%global commit 7317d88263fb9658cd7f1174c6bbcfb0a7ae856a
%global shortcommit %%(c=%{commit}; echo ${c:0:7})
%global date 20190429

%bcond_without check

Name: calypso
Version: 2.0
Release: 0.1.%{date}git%{shortcommit}%{?dist}
Summary: Free and open-source CalDAV calendar server
License: GPLv3+
URL: https://keithp.com/blogs/calypso/
Source0: %{name}-%{commit}.tar.xz
Source1: %{name}-mktarball.sh
Source2: %{name}.config
Source3: %{name}.pam
Source4: %{name}.systemd
# fix python-daemon dependency name
Patch0: %{name}-daemon.patch
BuildRequires: python3-daemon
BuildRequires: python3-devel
BuildRequires: python3-iniparse
BuildRequires: python3-vobject
BuildRequires: systemd-rpm-macros
%if %{with check}
BuildRequires: git-core
BuildRequires: python3-nose
%endif
Requires(pre): shadow-utils
Requires(post): git-core
Requires: git-core
Requires: python3-lockfile
Recommends: python3-kerberos
Recommends: python3-PyPAM
BuildArch: noarch

%description
Calypso is a python-based CalDAV/CardDAV server that started as a few small
patches to Radicale but was eventually split off as a separate project.

* Uses vObject for parsing and generating the data files
* Stores one event/contact per file
* Uses git to retain a history of the database

%prep
%setup -q -n %{name}-%{commit}
%patch0 -p1 -b .daemon

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_sharedstatedir}/calypso
install -Dpm644 calypso.1 %{buildroot}%{_mandir}/man1/calypso.1
install -Dpm644 %{S:2} %{buildroot}%{_sysconfdir}/calypso/config
install -Dpm644 %{S:3} %{buildroot}%{_sysconfdir}/pam.d/calypso
install -Dpm644 %{S:4} %{buildroot}%{_unitdir}/calypso.service

%if %{with check}
%check
nosetests-3
%endif

%pre
getent group calypso >/dev/null || groupadd -r calypso
getent passwd calypso >/dev/null || \
    useradd -r -g calypso -d %{_sharedstatedir}/calypso -s /sbin/nologin \
    -c "CalDAV/CardDAV server with git storage" calypso
exit 0

%preun
%systemd_preun calypso.service

%post
%systemd_post calypso.service
if [ $1 -eq 1 ] && ! [ -d %{_sharedstatedir}/calypso/default ]; then
    mkdir -p %{_sharedstatedir}/calypso/default
    pushd %{_sharedstatedir}/calypso/default
    cat > .calypso-collection << EOF
[collection]
is-calendar = 1
EOF
    git add .calypso-collection
    git commit -m'initialize new default calendar'
    popd
fi

%postun
%systemd_postun_with_restart calypso.service

%files
%license COPYING
%doc README collection-config config
%dir %attr(0750,root,calypso) %{_sysconfdir}/calypso
%config(noreplace) %{_sysconfdir}/calypso/config
%config(noreplace) %{_sysconfdir}/pam.d/calypso
%{_bindir}/calypso
%{_mandir}/man1/calypso.1*
%{_unitdir}/calypso.service
%{python3_sitelib}/calypso-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/calypso
%dir %attr(0750,calypso,calypso) %{_sharedstatedir}/calypso

%changelog
* Mon Mar 02 2020 Dominik Mierzejewski <dominik@greysector.net> 2.0-0.1.20190429git7317d88
- initial build
