# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1

Name:           sugar-kuku
Version:        5
Release:        14%{?dist}
Summary:        Based on the basic arithmetic education game Number Munchers

License:        GPLv3+
URL:            http://wiki.laptop.org/go/Kuku
Source0:        http://mirrors.mit.edu/sugarlabs/activities/4526/kuku_anakula-%{version}.xo

BuildRequires:  python2-devel sugar-toolkit gettext
BuildArch:      noarch
Requires:       sugar
Requires:       sugar-toolkit

%description
Based on the basic arithmetic education game Number Munchers.

%prep
%setup -q -n KukuAnakula.activity
sed -i -e '1i#!/usr/bin/python' kuku*.py
sed -i 's/python/python2/g' *.py

%build
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py install --prefix=%{buildroot}%{_prefix}

%files 
%license COPYING
%doc README 
%{sugaractivitydir}/KukuAnakula.activity/

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 5-10
- Fix build without python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 5-2
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 Danishka Navin <danishka@gmail.com> - 5-0
- Updated to latest version 5
- removed MANIFEST from %%doc

* Tue Aug 06 2013 Danishka Navin <danishka@gmail.com> - 4-8
- Fixed the BuildRequires as per suggestion of the review bug

* Tue Aug 06 2013 Danishka Navin <danishka@gmail.com> - 4-7
- removed #chmod +x  kuku_config.py

* Tue Aug 06 2013 Danishka Navin <danishka@gmail.com> - 4-6
- removed duplicate entries of changelog

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 4-5
- removed %%defattr(-,root,root,-)

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 4-4
- cheanged the License to GPLv3+

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 4-3
- added MANIFEST to %%doc files

* Tue Jul 17 2012 Danishka Navin <danishka@gmail.com> - 4-2
- added %%doc files

* Mon Jul 16 2012 Danishka Navin <danishka@gmail.com> - 4-1
- initial packaging

