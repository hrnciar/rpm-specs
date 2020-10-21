%if %{defined el6} || %{defined el7}
%global python      python
%else
%global __python    %{__python3}
%global python      python3
%endif

%if %{defined el6}
%global nosetests   nosetests
%else
%global nosetests   nosetests-%{python_version}
%bcond_without      systemd
%endif


Name:           nova-agent
Version:        2.1.21
Release:        4%{?dist}
Summary:        Agent for setting up clean servers on Xen
License:        ASL 2.0
URL:            https://github.com/Rackspace-DOT/nova-agent
Source0:        %{url}/archive/%{version}/nova-agent-%{version}.tar.gz
Patch0:         port-to-pycryptodomex.patch
BuildArch:      noarch

BuildRequires:  %{python}-devel
BuildRequires:  %{python}-setuptools
BuildRequires:  %{python}-nose
BuildRequires:  %{python}-pycryptodomex
BuildRequires:  %{python}-netifaces
BuildRequires:  %{python}-pyxs
BuildRequires:  %{python}-yaml
BuildRequires:  %{python}-distro
%if %{defined el6} || %{defined el7}
BuildRequires:  python-mock
%endif
%if %{defined el6}
BuildRequires:  python-unittest2
BuildRequires:  python-argparse
%endif

Requires:       %{python}-setuptools
Requires:       %{python}-pycryptodomex
Requires:       %{python}-netifaces
Requires:       %{python}-pyxs
Requires:       %{python}-yaml
Requires:       %{python}-distro
%if %{defined el6}
Requires:       python-argparse
%endif

%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif


%description
Python agent for setting up clean servers on Xen using xenstore data.


%prep
%autosetup -p 1


%build
%py_build


%install
%py_install

%if %{with systemd}
install -Dm644 etc/nova-agent.service %{buildroot}/%{_unitdir}/nova-agent.service
%else
install -Dm755 etc/nova-agent.redhat %{buildroot}/%{_initddir}/nova-agent
%endif


%check
%{nosetests} -v


%post
%if %{with systemd}
%systemd_post nova-agent.service
%else
chkconfig --add nova-agent &> /dev/null || :
%endif


%preun
%if %{with systemd}
%systemd_preun nova-agent.service
%else
if [ $1 -eq 0 ]; then
    service nova-agent stop &> /dev/null || :
    chkconfig --del nova-agent &> /dev/null || :
fi
%endif


%postun
%if %{with systemd}
%systemd_postun_with_restart nova-agent.service
%else
if [ $1 -ge 1 ]; then
    service nova-agent condrestart &> /dev/null || :
fi
%endif


%files
%license LICENSE
%doc README.md
%{python_sitelib}/novaagent
%{python_sitelib}/novaagent-%{version}-py%{python_version}.egg-info
%{_bindir}/nova-agent
%if %{with systemd}
%{_unitdir}/nova-agent.service
%else
%{_initddir}/nova-agent
%endif


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.21-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Carl George <carl@george.computer> - 2.1.21-1
- Latest upstream
- Add patch0 to switch to pycryptodomex

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.20-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.20-4
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Carl George <carl@george.computer> - 2.1.20-1
- Latest upstream
- Requires setuptools because the entrypoint script imports pkg_resources
- Use python3 on RHEL 8+

* Thu Sep 13 2018 Dave Kludt <david.kludt@rackspace.com> - 2.1.18-1
- Latest Upstream

* Wed Sep 05 2018 Dave Kludt <david.kludt@rackspace.com> - 2.1.17-1
- Latest Upstream

* Fri Aug 31 2018 Dave Kludt <david.kludt@rackspace.com> - 2.1.16-1
- Latest Upstream

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.14-2
- Rebuilt for Python 3.7

* Mon Jun 25 2018 Dave Kludt <david.kludt@rackspace.com> - 2.1.14-1
- Latest upstream

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.12-2
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Carl George <carl@george.computer> - 2.1.12-1
- Latest upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Carl George <carl@george.computer> - 2.1.11-1
- Latest upstream

* Tue Dec 19 2017 Carl George <carl@george.computer> - 2.1.10-1
- Latest upstream

* Sat Oct 21 2017 Carl George <carl@george.computer> - 2.1.8-1
- Latest upstream

* Tue Sep 05 2017 Carl George <carl@george.computer> - 2.1.6-1
- Latest upstream
- Add patch for pull request #22

* Thu Aug 31 2017 Carl George <carl@george.computer> - 2.1.5-1
- Latest upstream

* Thu Aug 10 2017 Carl George <carl@george.computer> - 2.1.1-1
- Latest upstream

* Wed Aug 09 2017 Carl George <carl@george.computer> - 2.1.0-1
- Latest upstream

* Wed Aug 02 2017 Carl George <carl@george.computer> - 2.0.3-1
- Latest upstream
- Run test suite

* Mon Jun 26 2017 Dave Kludt <david.kludt@rackspace.com> 2.0.0-1
- Refactor code and bump to higher version so upgrade can be done

* Mon Feb 15 2016 Daniel Wallace <danielwallace@gtmanfred.com> 0.2.1-1
- Always write a string to xenstore on returns

* Mon Feb 01 2016 Carl George <carl.george@rackspace.com> - 0.2.0-1
- Disable debug packages
- Build with Python 3 on Fedora and openSUSE
- openSUSE macros fixes

* Fri Jan 29 2016 Carl George <carl.george@rackspace.com> - 0.1.0-1
- Initial build of package
