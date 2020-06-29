%global pypi_name git-pull-request
%global pkg_name git_pull_request

Name:           %{pypi_name}
Version:        2.4.0
Release:        10%{?dist}
Summary:        Command line tool to send GitHub pull-request

License:        ASL 2.0
URL:            https://github.com/jd/git-pull-request
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
Requires:       python3-PyGithub
Requires:       python3-daiquiri
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}
 

%description
%{name} is a command line tool to send GitHub pull-request from
your terminal.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files
%doc README.rst
%{_bindir}/git-pull-request
%{python3_sitelib}/%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-10
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-7
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct  7 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 2.4.0-1
- Upstream 2.4.0
- Upstream dropped python2 support

* Thu May 25 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.0.2-1
- Initial package.
