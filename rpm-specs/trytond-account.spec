# -*- rpm-spec -*-
%global tryton_major 4.0
%global modname  account
%global pkgname %(echo \"%{name}\" | sed 's/-/_/g')

Name:           trytond-%{modname}
Version:        4.0.3
Release:        13%{?dist}
Summary:        %{modname} module for Tryton

License:        GPLv3+
URL:            http://www.tryton.org
Source0:        http://downloads.tryton.org/%{tryton_major}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       tryton(kernel) = %{tryton_major}
Requires:       trytond-company
Requires:       python3-simpleeval

%description
%{modname} module for Tryton application server.


%prep
%setup -q -n %{pkgname}-%{version}


%build
%py3_build


%install
%py3_install


%files
%doc CHANGELOG COPYRIGHT INSTALL LICENSE README
%{python3_sitelib}/trytond/modules/%{modname}/
%{python3_sitelib}/%{pkgname}-%{version}-*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-13
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-10
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 4.0.3-2
- Rebuild for Python 3.6

* Fri Sep 09 2016 Dan Horák <dan@danny.cz> - 4.0.3-1
- new upstream version 4.0.3

* Thu Jul 21 2016 Dan Horák <dan@danny.cz> - 4.0.1-1
- new upstream version 4.0.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 04 2013 Dan Horák <dan@danny.cz> - 2.6.2-1
- new upstream version 2.6.2

* Sat Oct 27 2012 Dan Horák <dan@danny.cz> - 2.6.1-1
- new upstream version 2.6.1

* Wed Sep 05 2012 Dan Horák <dan@danny.cz> - 2.4.2-1
- new upstream version 2.4.2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Dan Horák <dan@danny.cz> - 2.4.1-1
- new upstream version 2.4.1

* Sun Jan 15 2012 Dan Horák <dan@danny.cz> - 2.2.1-1
- new upstream version 2.2.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Dan Horák <dan@danny.cz> - 2.0.2-1
- new upstream version 2.0.2

* Mon Jun 06 2011 Dan Horák <dan@danny.cz> - 2.0.1-1
- new upstream version 2.0.1

* Tue May 03 2011 Dan Horák <dan@danny.cz> - 2.0.0-1
- new upstream version 2.0.0

* Mon Feb 21 2011 Dan Horák <dan[at]danny.cz> - 1.8.1-1
- updated to 1.8.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Dan Horák <dan[at]danny.cz> - 1.8.0-3
- initial Fedora package
