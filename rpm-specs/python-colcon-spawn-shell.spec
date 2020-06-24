%global srcname colcon-spawn-shell

Name:           python-%{srcname}
Version:        0.2.0
Release:        7%{?dist}
Summary:        Source colcon workspaces in a new shell

License:        ASL 2.0
URL:            https://github.com/colcon/colcon-spawn-shell
Source0:        https://github.com/colcon/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
This is a colcon plugin to chain workspaces in new shells. It allows quickly
un-chaining workspaces by exiting the spawned shell.

The shell's prompt is edited to show the workspace order. The only supported
shell is bash.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools >= 30.3.0
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-colcon-core >= 0.3.1
Requires:       python%{python3_pkgversion}-colcon-bash >= 0.3.0
%endif # __pythondist_requires

%description -n python%{python3_pkgversion}-%{srcname}
This is a colcon plugin to chain workspaces in new shells. It allows quickly
un-chaining workspaces by exiting the spawned shell.

The shell's prompt is edited to show the workspace order. The only supported
shell is bash.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/colcon_spawn_shell/
%{python3_sitelib}/colcon_spawn_shell-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Scott K Logan <logans@cottsay.net> - 0.2.0-2
- Fix changelog version

* Fri Apr 26 2019 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Rebuilt to change main python from 3.4 to 3.6 in EPEL 7
- Handle automatic dependency generation (f30+)

* Fri Nov 09 2018 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Initial package
