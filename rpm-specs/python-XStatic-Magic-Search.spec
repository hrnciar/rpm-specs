%global pypi_name XStatic-Magic-Search

Name:           python-%{pypi_name}
Version:        0.2.5.1
Release:        14%{?dist}
Summary:        Magic-Search (XStatic packaging standard)

License:        ASL 2.0
URL:            https://github.com/eucalyptus/magic-search
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%package -n python3-%{pypi_name}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  web-assets-devel

Requires:       python3-XStatic
Requires:       XStatic-Magic-Search-common = %{version}-%{release}

Summary:        Magic-Search (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
MagicSearch is an AngularJS directive that provides a UI for both faceted
filtering and as-you-type filtering. It is intended for filtering tables,
such as an AngularJS smart-table, but it can be used in any situation
where you can provide it with facets/options and consume its events.

%package -n XStatic-Magic-Search-common
Summary:        Xstatic-Magic-Search common files
Requires:       web-assets-filesystem
%description -n XStatic-Magic-Search-common
Xstatic-Magic-Search common files

%prep
%autosetup -n %{pypi_name}-%{version}

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/magic_search'|" xstatic/pkg/magic_search/__init__.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}/%{_jsdir}/magic_search
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/magic_search/data/magic_search.* %{buildroot}/%{_jsdir}/magic_search

%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/magic_search
%{python3_sitelib}/XStatic_Magic_Search-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_Magic_Search-%{version}-py%{python3_version}-nspkg.pth

%files -n XStatic-Magic-Search-common
%{_jsdir}/magic_search


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.5.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.5.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.5.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.5.1-8
- Subpackage python2-XStatic-Magic-Search has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.5.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5.1-2
- Rebuild for Python 3.6

* Wed Aug 31 2016 Matthias Runge <mrunge@redhat.com> - 0.2.5.1-1
- update package, add python3 subpackage (rhbz#1210069)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

>>>>>>> f5864c96ae5709602069a2b35170e0ec84cea720
* Mon Mar 23 2015 Matthias Runge <mrunge@redhat.com> - 0.2.0.1-1
- Initial package. (rhbz#1204779)
