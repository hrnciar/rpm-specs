%global upstream_name aiohttp-negotiate
%global modname aiohttp_negotiate

Name:           python-%{upstream_name}
Version:        0.11
Release:        13%{?dist}
Summary:        Add-on for Python aiohttp library to support Negotiate authentication
License:        BSD
URL:            https://github.com/ox-it/aiohttp-negotiate
Source0:        https://github.com/ox-it/%{upstream_name}/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
# https://github.com/ox-it/aiohttp-negotiate/pull/1
Source1:        https://raw.githubusercontent.com/danc86/aiohttp-negotiate/350ac51ba0ab0b871d39c975af27d027e35f514e/LICENSE
BuildArch:      noarch

%global _description \
A mixin for supporting Negotiate authentication with aiohttp.

%description %{_description}

%package -n python%{python3_pkgversion}-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-www-authenticate
Requires:       python%{python3_pkgversion}-gssapi

%description -n python%{python3_pkgversion}-%{upstream_name} %{_description}

Python %{python3_pkgversion} version.

%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{upstream_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{upstream_name}}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
Requires:       python%{python3_other_pkgversion}-aiohttp
Requires:       python%{python3_other_pkgversion}-www-authenticate
Requires:       python%{python3_other_pkgversion}-gssapi

%description -n python%{python3_other_pkgversion}-%{upstream_name} %{_description}

Python %{python3_other_pkgversion} version.
%endif

%prep
%autosetup -n %{upstream_name}-%{version}
cp -p %{SOURCE1} .

%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif

%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif

%check
# No tests. :-(

%files -n python%{python3_pkgversion}-%{upstream_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{modname}.py*
%{python3_sitelib}/__pycache__/%{modname}.*
%{python3_sitelib}/%{modname}-*.egg-info

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{upstream_name}
%license LICENSE
%doc README.rst
%{python3_other_sitelib}/%{modname}.py*
%{python3_other_sitelib}/__pycache__/%{modname}.*
%{python3_other_sitelib}/%{modname}-*.egg-info
%endif

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 08 2016 Dan Callaghan <dcallagh@redhat.com> - 0.11-1
- initial version
