Name:           regindexer
Version:        0.6.2
Release:        3%{?dist}
Summary:        Tool for creating an index of a container registry

License:        MIT
URL:            https://pagure.io/regindexer
Source0:        https://releases.pagure.org/regindexer/regindexer-%{version}.tar.gz
Source1:        regindexer.service

BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  systemd

%?python_enable_dependency_generator

%description
regindexer is a tool for creating an index of a container registry. It can
be run manually from the command line, or can run run as a daemon
rebuilding the index when it sees messages from Bodhi.

%prep
%autosetup


%build
%py3_build


%install
%py3_install
install -p -m 0644 -D config-example.yaml $RPM_BUILD_ROOT%{_sysconfdir}/regindexer/config.yaml
install -p -m 0755 -d $RPM_BUILD_ROOT%{_sharedstatedir}/regindexer

install -p -m 0644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/regindexer.service

%pre
getent group regindexer >/dev/null || groupadd -r regindexer
getent passwd regindexer >/dev/null || \
    useradd -r -g regindexer -d %{_sharedstatedir}/regindexer -s /sbin/nologin \
    -c "regindexer daemon user" regindexer
exit 0

%post
%systemd_post regindexer.service

%preun
%systemd_preun regindexer.service

%postun
%systemd_postun_with_restart regindexer.service

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/regindexer/
%{python3_sitelib}/regindexer*.egg-info/
%{_bindir}/regindexer
%{_bindir}/regindexer-daemon
%{_unitdir}/*
%config(noreplace) %{_sysconfdir}/regindexer
%attr(-, regindexer, regindexer) %{_sharedstatedir}/regindexer

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.9

* Tue Feb  4 2020 Owen Taylor <otaylor@redhat.com> - 0.6.2-1
- Version 0.6.2 - make required_labels work correctly

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Owen Taylor <otaylor@redhat.com> - 0.6-1
- Version 0.6 (add support for Flatpak metadata in labels)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5-5
- Rebuilt for Python 3.8

* Thu Aug  8 2019 fedora-toolbox <otaylor@redhat.com> - 0.5-4
- Use python_enable_dependency_generator (from Igor Gnatenko)
- Use install -p to preserve timestamps (also from Igor Gnatenko)

* Mon Aug  5 2019 Owen Taylor <otaylor@redhat.com> - 0.5-3
- Switch back to Python 3 (resolves #1655256)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun  6 2019 fedora-toolbox <otaylor@redhat.com> - 0.5-1
- Version 0.5 (compatibility with Bodhi v4)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 fedora-toolbox <otaylor@redhat.com> - 0.4-1
- Version 0.4 (fixes problem with > 100 repositories)

* Wed Aug 29 2018 Owen Taylor <otaylor@redhat.com> - 0.3-1
- Version 0.3

* Sat Aug 11 2018 Owen Taylor <otaylor@redhat.com> - 0.2-1
- Version 0.2 - switch from fedmsg-hub plugin to a daemon

* Thu Aug  2 2018 Owen Taylor <otaylor@redhat.com> - 0.1-1
- Initial version
