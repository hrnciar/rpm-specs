# -*- rpm-spec -*-
%global tryton_major 4.0
%global modname  account-stock-continental
%global pkgname %(echo \"%{name}\" | sed 's/-/_/g')

Name:           trytond-%{modname}
Version:        4.0.1
Release:        14%{?dist}
Summary:        %{modname} module for Tryton

License:        GPLv3+
URL:            http://www.tryton.org
Source0:        http://downloads.tryton.org/%{tryton_major}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       tryton(kernel) = %{tryton_major}
Requires:       trytond-account-product
Requires:       trytond-stock

%description
%{modname} module for Tryton application server.


%prep
%setup -q -n %{pkgname}-%{version}

rm -rf %{pkgname}.egg-info


%build
%py3_build


%install
%py3_install


%files
%doc CHANGELOG COPYRIGHT LICENSE README
%doc doc
%{python3_sitelib}/trytond/modules/*/
%{python3_sitelib}/%{pkgname}-%{version}-*.egg-info/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-13
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-10
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-2
- Rebuild for Python 3.6

* Fri Aug 05 2016 Dan Horák <dan@danny.cz> - 4.0.1-1
- new upstream version 4.0.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Dan Horák <dan@danny.cz> - 2.6.1-1
- new upstream version 2.6.1

* Sat Nov 17 2012 Dan Horák <dan@danny.cz> - 2.4.2-4
- don't include INSTALL as documentation, it's redundant

* Sun Oct 07 2012 Dan Horák <dan@danny.cz> - 2.4.2-3
- remove upstream egginfo

* Tue Sep 11 2012 Dan Horák <dan@danny.cz> - 2.4.2-2
- spec cleanup

* Mon Sep 10 2012 Dan Horák <dan@danny.cz> - 2.4.2-1
- new upstream version 2.4.2

* Mon Jan 16 2012 Dan Horák <dan@danny.cz> - 2.2.0-1
- new upstream version 2.2.0

* Wed Jun 08 2011 Dan Horák <dan[at]danny.cz> - 2.0.0-1
- initial Fedora package
