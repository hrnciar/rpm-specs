Name:           cdbs
Version:        0.4.162
Release:        1%{?dist}
Summary:        Common build system for Debian packages
BuildArch:      noarch

License:        GPLv2+
URL:            https://salsa.debian.org/build-common-team/cdbs
Source0:        http://ftp.de.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz

# waf-unpack python3 fixes
Patch0:         cdbs_py3.patch
BuildRequires:  perl-generators

%description
This package contains the Common Debian Build System, an abstract build system
based on Makefile inheritance which is completely extensible and overridable.
In other words, CDBS provides a sane set of default rules upon which packages
can build; any or all rules may be overridden as needed.

%prep
%setup -q -n %{name}-%{version}
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 8
%patch0 -p1
%endif


%build
%configure
%make_build


%install
%make_install


#check
# Although the Makefile has a check rule, it requires a functional
# dpkg-checkbuilddeps, which is not the case on Fedora.


%files
%doc TODO
%license COPYING
%{_bindir}/cdbs-edit-patch
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/cdbs-edit-patch.1*

%changelog
* Sun Apr 26 2020 Sandro Mani <manisandro@gmail.com> - 0.4.162-1
- Update to 0.4.162

* Sun Apr 12 2020 Sandro Mani <manisandro@gmail.com> - 0.4.161-1
- Update to 0.4.161

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.159-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Sérgio Basto <sergio@serjux.com> - 0.4.159-3
- Fix build for epel8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.159-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Sandro Mani <manisandro@gmail.com> - 0.4.159-1
- Update to 0.4.159

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.158-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Sandro Mani <manisandro@gmail.com> - 0.4.158-1
- Update to 0.4.158

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.156-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.156-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Sandro Mani <manisandro@gmail.com> - 0.4.156-1
- Update to 0.4.156

* Sun Oct 08 2017 Sandro Mani <manisandro@gmail.com> - 0.4.153-1
- Update to 0.4.153

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.152-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Sandro Mani <manisandro@gmail.com> - 0.4.152-1
- Update to 0.4.152

* Fri Jun 02 2017 Sandro Mani <manisandro@gmail.com> - 0.4.151-1
- Update to 0.4.151

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.150-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.150-2
- Rebuild for Python 3.6

* Mon Nov 21 2016 Sandro Mani <manisandro@gmail.com> - 0.4.150-1
- Update to 0.4.150

* Wed Sep 28 2016 Sandro Mani <manisandro@gmail.com> - 0.4.148-1
- Update to 0.4.148

* Thu Sep 15 2016 Sandro Mani <manisandro@gmail.com> - 0.4.146-1
- Update to 0.4.146

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 0.4.143-1
- Update to 0.4.143

* Tue Jun 28 2016 Sandro Mani <manisandro@gmail.com> - 0.4.142-1
- Update to 0.4.142

* Mon Jun 13 2016 Sandro Mani <manisandro@gmail.com> - 0.4.139-1
- Update to 0.4.139

* Tue May 24 2016 Sandro Mani <manisandro@gmail.com> - 0.4.137-1
- Update to 0.4.137

* Thu May 12 2016 Sandro Mani <manisandro@gmail.com> - 0.4.131-1
- Update to 0.4.131

* Sun Mar 06 2016 Sandro Mani <manisandro@gmail.com> - 0.4.130-4
- Port waf-unpack to python3, keep compatibility with python2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.130-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Sandro Mani <manisandro@gmail.com> - 0.4.130-1
- Update to 0.4.130

* Tue Mar 17 2015 Sandro Mani <manisandro@gmail.com> - 0.4.129-1
- Update to 0.4.129

* Fri Mar 06 2015 Sandro Mani <manisandro@gmail.com> - 0.4.128-1
- Update to 0.4.128

* Wed Oct 15 2014 Sandro Mani <manisandro@gmail.com> ⁻ 0.4.127-1
- Update to 0.4.127

* Sat Aug 23 2014 Sandro Mani <manisandro@gmail.com> - 0.4.126-1
- Update to 0.4.126

* Mon Jun 23 2014 Sandro Mani <manisandro@gmail.com> - 0.4.125-1
- Update to 0.4.125

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Sandro Mani <manisandro@gmail.com> - 0.4.123-1
- Update to 0.4.123

* Wed Feb 19 2014 Sandro Mani <manisandro@gmail.com> - 0.4.122-2
- Make package noarch

* Sun Feb  9 2014 Sandro Mani <manisandro@gmail.com> - 0.4.122-1
- Initial package
