Name:		cv-zabbix-checks	
Version:	0.9
Release:	1%{?dist}
Summary:	Zabbix checks by CLusterVision

Group:		CV	
License:	GPLv3.0
URL:		http://github.com/krumstein/trinityX
Source0:	%name-%version.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	zabbix-agent
%description
ClusterVision Zabbix checks

%prep
%setup -q


%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/zabbix
install -m 0755 -d $RPM_BUILD_ROOT/var/lib/zabbix/userparameters
install -m 0755 userparameters/* $RPM_BUILD_ROOT/var/lib/zabbix/userparameters/

install -m 0755 -d $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/
install -m 0644 zabbix_agentd.d/* $RPM_BUILD_ROOT/etc/zabbix/zabbix_agentd.d/

install -m 0755 -d $RPM_BUILD_ROOT/etc/sudoers.d/
install -m 0644 sudoers-zabbix $RPM_BUILD_ROOT/etc/sudoers.d/zabbix

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/templates/
install -m 0644  templates/*.xml $RPM_BUILD_ROOT/usr/lib/zabbix/templates/

install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/utils
install -m 0755 utils/import.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/
install -m 0755 utils/add_group.sh $RPM_BUILD_ROOT/usr/lib/zabbix/utils/


install -m 0755 -d $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
install -m 0755 externalscripts/* $RPM_BUILD_ROOT/usr/lib/zabbix/externalscripts/
mkdir $RPM_BUILD_ROOT/tmp
touch $RPM_BUILD_ROOT/tmp/ipmitool.cache

%clean
rm -rf $RPM_BUILD_ROOT
%post
systemctl restart zabbix-agent


%files
%dir %attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters
%attr(-,zabbix,zabbix) /var/lib/zabbix/userparameters/*

%attr(-,root,root) /etc/zabbix/zabbix_agentd.d/*

%attr(-,root,root) /etc/sudoers.d/zabbix
%attr(-,root,root) /usr/lib/zabbix/externalscripts/*
%attr(-,root,root) /tmp/ipmitool.cache
%attr(-,root,root) /usr/lib/zabbix/templates/*
%attr(-,root,root) /usr/lib/zabbix/utils/*

%doc



%changelog
* Thu Nov 17 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.9
- Updated templates, standart timeouts
* Tue Nov 15 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.8
- Added storcli
* Tue Nov 15 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.7
- Added sas3ircu and simplified spec file
* Thu Nov 10 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.6
- Added add_group.sh script and moved import.sh to utils directory
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5.3
- Added opa hfi monitoring
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5.1
- Added accessibilty of mount check
* Fri Nov 04 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.5
- Added mounts checks via systemd
* Fri Oct 28 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.1
- Initial RPM release 
* Fri Oct 28 2016 Vladimir Krumshtein <vladimir.krumstein@clustervision.com> 0.2
- Added external checks

