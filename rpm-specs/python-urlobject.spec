Name: python-urlobject
Summary: A utility class for manipulating URLs
Version: 2.4.3
Release: 14%{?dist}
BuildArch:  noarch
Source0: https://pypi.python.org/packages/source/U/URLObject/URLObject-%{version}.tar.gz
License: Unlicense

Url: http://github.com/zacharyvoase/urlobject

Patch10:  remove-six.patch


%description
A utility class for manipulating URLs


%package -n python3-urlobject
Summary: A utility class for manipulating URLs
BuildRequires:  python3-six
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:  python3-six
%description -n python3-urlobject
A utility class for manipulating URLs


%prep
%setup -q -n URLObject-%{version}
%patch10


%build
%py3_build


%install
%py3_install


%files -n python3-urlobject
%license UNLICENSE
%{python3_sitelib}/urlobject/
%{python3_sitelib}/URLObject*.egg-info


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-6
- Rebuilt for Python 3.7

* Thu Mar 22 2018 John Dulaney <jdulaney@fedoraproject.org> - 2.4.3-5
- Drop python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.4.3-3
- Fix typo in spec and clean up a bit

* Thu Aug 17 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.4.3-2
- Update patch to remove bundled six

* Tue Aug 15 2017 John Dulaney <jdulaney@fedoraproject.org> - 2.4.3-1
- Update to newest upstream release
- Ship python2-urlobject

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 2.4.0-6
- Correct typo

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 2.4.0-5
- Prepare for epel submission

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 24 2015 John Dulaney <jdulaney@fedoraproject.org> - 2.4.0-3
- Initial Packaging
