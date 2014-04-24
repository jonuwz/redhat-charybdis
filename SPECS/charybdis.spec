Name: charybdis
Version: 3.4.2
Release: 1
Summary: a highly-scalable ircv3-compliant irc daemon
BuildArch: x86_64
AutoReqProv: no
BuildRoot: %buildroot
Prefix: /opt/ircd
Group: default
License: unknown
Vendor: Atheme
URL: http://www.atheme.org/projects/charybdis.html
Packager: santa@northpole.com
Requires: openssl
BuildRequires: bison flex openssl-devel
Source0: https://github.com/atheme/charybdis/archive/%{name}-%{version}.tar.gz
Source1: ircd.init
Source2: ircd.conf
%description
charybdis is an ircd used on various networks either as itself, or as the
basis of a customized IRC server implementation.
A derivative of charybdis, ircd-seven powers freenode, which is the 
largest IRC network in the world.

%prep
cd %{_topdir}/BUILD
rm -rf %{name}-%{version}
/usr/bin/gzip -dc %{_topdir}/SOURCES/%{name}-%{version}.tar.gz | /bin/tar -xvvf -
STATUS=$?
if [ $STATUS -ne 0 ]; then
  exit $STATUS
fi
[[ -d %{name}-%{name}-%{version} ]] && mv %{name}-%{name}-%{version} %{name}-%{version}
cd %{name}-%{version}
/bin/chmod -Rf a+rX,u+w,g-w,o-w .

%build
cd %{name}-%{version}
./configure --with-logdir=/var/log/ircd --enable-openssl --with-rundir=/var/run/ircd --prefix /opt/ircd --sysconfdir /etc/ircd
make

%pre 
getent group ircd >/dev/null || groupadd ircd || exit 1
getent passwd ircd >/dev/null || useradd -m -d /opt/ircd -s /bin/false -g ircd ircd || exit 1

%install
cd %{name}-%{version}
make DESTDIR=$RPM_BUILD_ROOT install
mkdir $RPM_BUILD_ROOT/etc/init.d
install -m 755 %{_topdir}/SOURCES/ircd.init $RPM_BUILD_ROOT/etc/init.d/ircd
install -m 640 %{_topdir}/SOURCES/ircd.conf $RPM_BUILD_ROOT/etc/ircd/ircd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %attr(0750,ircd,root) /var/log/ircd
%dir %attr(0750,ircd,root) /etc/ircd
%dir %attr(0750,ircd,root) /var/run/ircd
%config(noreplace) %attr(0640,root,ircd) %{_sysconfdir}/ircd/ircd.conf
%config(noreplace) %attr(0640,root,ircd) %{_sysconfdir}/ircd/ircd.motd
%attr(0755,root,root) /etc/init.d/ircd
%attr(0640,root,ircd) %{_sysconfdir}/ircd/reference.conf
%attr(0640,root,ircd) %{_sysconfdir}/ircd/example.conf
/opt/ircd/bin/bandb
/opt/ircd/bin/bantool
/opt/ircd/bin/convertilines
/opt/ircd/bin/convertklines
/opt/ircd/bin/genssl.sh
/opt/ircd/bin/ircd
/opt/ircd/bin/mkpasswd
/opt/ircd/bin/ssld
/opt/ircd/bin/viconf
/opt/ircd/bin/vimotd
/opt/ircd/help/opers/accept
/opt/ircd/help/opers/admin
/opt/ircd/help/opers/away
/opt/ircd/help/opers/capab
/opt/ircd/help/opers/challenge
/opt/ircd/help/opers/chantrace
/opt/ircd/help/opers/close
/opt/ircd/help/opers/cmode
/opt/ircd/help/opers/cnotice
/opt/ircd/help/opers/connect
/opt/ircd/help/opers/cprivmsg
/opt/ircd/help/opers/credits
/opt/ircd/help/opers/die
/opt/ircd/help/opers/dline
/opt/ircd/help/opers/error
/opt/ircd/help/opers/etrace
/opt/ircd/help/opers/extban
/opt/ircd/help/opers/help
/opt/ircd/help/opers/index
/opt/ircd/help/opers/info
/opt/ircd/help/opers/invite
/opt/ircd/help/opers/ison
/opt/ircd/help/opers/join
/opt/ircd/help/opers/kick
/opt/ircd/help/opers/kill
/opt/ircd/help/opers/kline
/opt/ircd/help/opers/knock
/opt/ircd/help/opers/links
/opt/ircd/help/opers/list
/opt/ircd/help/opers/locops
/opt/ircd/help/opers/lusers
/opt/ircd/help/opers/map
/opt/ircd/help/opers/masktrace
/opt/ircd/help/opers/modlist
/opt/ircd/help/opers/modload
/opt/ircd/help/opers/modreload
/opt/ircd/help/opers/modrestart
/opt/ircd/help/opers/modunload
/opt/ircd/help/opers/motd
/opt/ircd/help/opers/names
/opt/ircd/help/opers/nick
/opt/ircd/help/opers/notice
/opt/ircd/help/opers/oper
/opt/ircd/help/opers/operspy
/opt/ircd/help/opers/operwall
/opt/ircd/help/opers/part
/opt/ircd/help/opers/pass
/opt/ircd/help/opers/ping
/opt/ircd/help/opers/pong
/opt/ircd/help/opers/post
/opt/ircd/help/opers/privmsg
/opt/ircd/help/opers/privs
/opt/ircd/help/opers/quit
/opt/ircd/help/opers/rehash
/opt/ircd/help/opers/restart
/opt/ircd/help/opers/resv
/opt/ircd/help/opers/scan
/opt/ircd/help/opers/server
/opt/ircd/help/opers/set
/opt/ircd/help/opers/sjoin
/opt/ircd/help/opers/snomask
/opt/ircd/help/opers/squit
/opt/ircd/help/opers/stats
/opt/ircd/help/opers/svinfo
/opt/ircd/help/opers/testgecos
/opt/ircd/help/opers/testline
/opt/ircd/help/opers/testmask
/opt/ircd/help/opers/time
/opt/ircd/help/opers/topic
/opt/ircd/help/opers/trace
/opt/ircd/help/opers/uhelp
/opt/ircd/help/opers/umode
/opt/ircd/help/opers/undline
/opt/ircd/help/opers/unkline
/opt/ircd/help/opers/unreject
/opt/ircd/help/opers/unresv
/opt/ircd/help/opers/unxline
/opt/ircd/help/opers/user
/opt/ircd/help/opers/userhost
/opt/ircd/help/opers/users
/opt/ircd/help/opers/version
/opt/ircd/help/opers/wallops
/opt/ircd/help/opers/who
/opt/ircd/help/opers/whois
/opt/ircd/help/opers/whowas
/opt/ircd/help/opers/xline
/opt/ircd/help/users/accept
/opt/ircd/help/users/admin
/opt/ircd/help/users/away
/opt/ircd/help/users/challenge
/opt/ircd/help/users/chantrace
/opt/ircd/help/users/cmode
/opt/ircd/help/users/cnotice
/opt/ircd/help/users/cprivmsg
/opt/ircd/help/users/credits
/opt/ircd/help/users/error
/opt/ircd/help/users/extban
/opt/ircd/help/users/help
/opt/ircd/help/users/index
/opt/ircd/help/users/info
/opt/ircd/help/users/invite
/opt/ircd/help/users/ison
/opt/ircd/help/users/join
/opt/ircd/help/users/kick
/opt/ircd/help/users/knock
/opt/ircd/help/users/links
/opt/ircd/help/users/list
/opt/ircd/help/users/lusers
/opt/ircd/help/users/map
/opt/ircd/help/users/motd
/opt/ircd/help/users/names
/opt/ircd/help/users/nick
/opt/ircd/help/users/notice
/opt/ircd/help/users/oper
/opt/ircd/help/users/part
/opt/ircd/help/users/pass
/opt/ircd/help/users/ping
/opt/ircd/help/users/pong
/opt/ircd/help/users/privmsg
/opt/ircd/help/users/quit
/opt/ircd/help/users/stats
/opt/ircd/help/users/time
/opt/ircd/help/users/topic
/opt/ircd/help/users/trace
/opt/ircd/help/users/umode
/opt/ircd/help/users/user
/opt/ircd/help/users/userhost
/opt/ircd/help/users/users
/opt/ircd/help/users/version
/opt/ircd/help/users/who
/opt/ircd/help/users/whois
/opt/ircd/help/users/whowas
/opt/ircd/lib/libratbox.la
/opt/ircd/lib/libratbox.so
/opt/ircd/lib/pkgconfig/libratbox.pc
/opt/ircd/modules/autoload/m_accept.so
/opt/ircd/modules/autoload/m_admin.so
/opt/ircd/modules/autoload/m_away.so
/opt/ircd/modules/autoload/m_cap.so
/opt/ircd/modules/autoload/m_capab.so
/opt/ircd/modules/autoload/m_certfp.so
/opt/ircd/modules/autoload/m_challenge.so
/opt/ircd/modules/autoload/m_chghost.so
/opt/ircd/modules/autoload/m_close.so
/opt/ircd/modules/autoload/m_cmessage.so
/opt/ircd/modules/autoload/m_connect.so
/opt/ircd/modules/autoload/m_dline.so
/opt/ircd/modules/autoload/m_encap.so
/opt/ircd/modules/autoload/m_etrace.so
/opt/ircd/modules/autoload/m_help.so
/opt/ircd/modules/autoload/m_info.so
/opt/ircd/modules/autoload/m_invite.so
/opt/ircd/modules/autoload/m_ison.so
/opt/ircd/modules/autoload/m_kline.so
/opt/ircd/modules/autoload/m_knock.so
/opt/ircd/modules/autoload/m_links.so
/opt/ircd/modules/autoload/m_list.so
/opt/ircd/modules/autoload/m_locops.so
/opt/ircd/modules/autoload/m_lusers.so
/opt/ircd/modules/autoload/m_map.so
/opt/ircd/modules/autoload/m_monitor.so
/opt/ircd/modules/autoload/m_motd.so
/opt/ircd/modules/autoload/m_names.so
/opt/ircd/modules/autoload/m_oper.so
/opt/ircd/modules/autoload/m_operspy.so
/opt/ircd/modules/autoload/m_pass.so
/opt/ircd/modules/autoload/m_ping.so
/opt/ircd/modules/autoload/m_pong.so
/opt/ircd/modules/autoload/m_post.so
/opt/ircd/modules/autoload/m_privs.so
/opt/ircd/modules/autoload/m_rehash.so
/opt/ircd/modules/autoload/m_restart.so
/opt/ircd/modules/autoload/m_resv.so
/opt/ircd/modules/autoload/m_sasl.so
/opt/ircd/modules/autoload/m_scan.so
/opt/ircd/modules/autoload/m_services.so
/opt/ircd/modules/autoload/m_set.so
/opt/ircd/modules/autoload/m_signon.so
/opt/ircd/modules/autoload/m_snote.so
/opt/ircd/modules/autoload/m_stats.so
/opt/ircd/modules/autoload/m_svinfo.so
/opt/ircd/modules/autoload/m_tb.so
/opt/ircd/modules/autoload/m_testline.so
/opt/ircd/modules/autoload/m_testmask.so
/opt/ircd/modules/autoload/m_tginfo.so
/opt/ircd/modules/autoload/m_time.so
/opt/ircd/modules/autoload/m_topic.so
/opt/ircd/modules/autoload/m_trace.so
/opt/ircd/modules/autoload/m_unreject.so
/opt/ircd/modules/autoload/m_user.so
/opt/ircd/modules/autoload/m_userhost.so
/opt/ircd/modules/autoload/m_users.so
/opt/ircd/modules/autoload/m_version.so
/opt/ircd/modules/autoload/m_wallops.so
/opt/ircd/modules/autoload/m_who.so
/opt/ircd/modules/autoload/m_whois.so
/opt/ircd/modules/autoload/m_whowas.so
/opt/ircd/modules/autoload/m_xline.so
/opt/ircd/modules/autoload/sno_routing.so
/opt/ircd/modules/extensions/chm_adminonly.so
/opt/ircd/modules/extensions/chm_operonly.so
/opt/ircd/modules/extensions/chm_operonly_compat.so
/opt/ircd/modules/extensions/chm_quietunreg_compat.so
/opt/ircd/modules/extensions/chm_sslonly.so
/opt/ircd/modules/extensions/chm_sslonly_compat.so
/opt/ircd/modules/extensions/createauthonly.so
/opt/ircd/modules/extensions/createoperonly.so
/opt/ircd/modules/extensions/example_module.so
/opt/ircd/modules/extensions/extb_account.so
/opt/ircd/modules/extensions/extb_canjoin.so
/opt/ircd/modules/extensions/extb_channel.so
/opt/ircd/modules/extensions/extb_extgecos.so
/opt/ircd/modules/extensions/extb_oper.so
/opt/ircd/modules/extensions/extb_realname.so
/opt/ircd/modules/extensions/extb_server.so
/opt/ircd/modules/extensions/extb_ssl.so
/opt/ircd/modules/extensions/extb_usermode.so
/opt/ircd/modules/extensions/force_user_invis.so
/opt/ircd/modules/extensions/hurt.so
/opt/ircd/modules/extensions/ip_cloaking.so
/opt/ircd/modules/extensions/ip_cloaking_3.0.so
/opt/ircd/modules/extensions/ip_cloaking_4.0.so
/opt/ircd/modules/extensions/ip_cloaking_old.so
/opt/ircd/modules/extensions/m_42.so
/opt/ircd/modules/extensions/m_adminwall.so
/opt/ircd/modules/extensions/m_findforwards.so
/opt/ircd/modules/extensions/m_identify.so
/opt/ircd/modules/extensions/m_mkpasswd.so
/opt/ircd/modules/extensions/m_ojoin.so
/opt/ircd/modules/extensions/m_okick.so
/opt/ircd/modules/extensions/m_olist.so
/opt/ircd/modules/extensions/m_omode.so
/opt/ircd/modules/extensions/m_opme.so
/opt/ircd/modules/extensions/m_remove.so
/opt/ircd/modules/extensions/m_roleplay.so
/opt/ircd/modules/extensions/m_sendbans.so
/opt/ircd/modules/extensions/m_webirc.so
/opt/ircd/modules/extensions/no_locops.so
/opt/ircd/modules/extensions/no_oper_invis.so
/opt/ircd/modules/extensions/override.so
/opt/ircd/modules/extensions/sno_farconnect.so
/opt/ircd/modules/extensions/sno_globalkline.so
/opt/ircd/modules/extensions/sno_globaloper.so
/opt/ircd/modules/extensions/sno_whois.so
/opt/ircd/modules/extensions/spy_admin_notice.so
/opt/ircd/modules/extensions/spy_info_notice.so
/opt/ircd/modules/extensions/spy_links_notice.so
/opt/ircd/modules/extensions/spy_motd_notice.so
/opt/ircd/modules/extensions/spy_stats_notice.so
/opt/ircd/modules/extensions/spy_stats_p_notice.so
/opt/ircd/modules/extensions/spy_trace_notice.so
/opt/ircd/modules/m_ban.so
/opt/ircd/modules/m_die.so
/opt/ircd/modules/m_error.so
/opt/ircd/modules/m_join.so
/opt/ircd/modules/m_kick.so
/opt/ircd/modules/m_kill.so
/opt/ircd/modules/m_message.so
/opt/ircd/modules/m_mode.so
/opt/ircd/modules/m_nick.so
/opt/ircd/modules/m_part.so
/opt/ircd/modules/m_quit.so
/opt/ircd/modules/m_server.so
/opt/ircd/modules/m_squit.so
/opt/ircd/share/man/man8/ircd.8

