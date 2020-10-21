%global commit 524d5d36bdedc4995f06cdefaaa82546c41a75c2
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global pkgname modestmaps
%global srcname ModestMaps

Name:           python-%{pkgname}
Version:        1.4.7
Release:        8%{?dist}
Summary:        Modest Maps python port

License:        BSD
URL:            http://modestmaps.com
Source0:        https://github.com/stamen/%{pkgname}-py/archive/%{commit}/%{pkgname}-py-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
Modest Maps is a small, extensible, and free library for designers and
developers who want to use interactive maps in their own projects. It provides
a core set of features in a tight, clean package with plenty of hooks for
additional functionality.


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-imaging

%{?python_provide:%python_provide python%{python3_pkgversion}-modestmaps}

%description -n python%{python3_pkgversion}-%{pkgname}
Modest Maps is a small, extensible, and free library for designers and
developers who want to use interactive maps in their own projects. It provides
a core set of features in a tight, clean package with plenty of hooks for
additional functionality.

%prep
%autosetup -p1 -n %{pkgname}-py-%{commit}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pkgname}
%doc CHANGELOG
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 05 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.7-5
- Subpackage python2-modestmaps has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 16 2018 Scott K Logan <logans@cottsay.net> - 1.4.7-1
- Update to 1.4.7
- Add python3 package
- Switch to Github upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Scott K Logan <logans@cottsay.net> - 1.4.6-6
- Update to latest Fedora packaging guidelines

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 Scott K Logan <logans@cottsay.net> - 1.4.6-2
- Clean-ups from package review

* Sun Sep 28 2014 Scott K Logan <logans@cottsay.net> - 1.4.6-1
- Initial package
