Name:           unar
Version:        1.10.1
Release:        17%{dist}
Summary:        Multi-format extractor
License:        LGPLv2+
URL:            https://theunarchiver.com/command-line
Source0:        http://unarchiver.c3.cx/downloads/unar%{version}_src.zip
BuildRequires:  bzip2-devel
BuildRequires:  gcc-objc
BuildRequires:  gcc-c++
BuildRequires:  gnustep-base-devel
BuildRequires:  libicu-devel
BuildRequires:  zlib-devel

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv5, RAR support includes
encryption and multiple volumes, unar can serve as a free and open source
replacement of unrar.

%prep
%setup -q -c
mv The\ Unarchiver/* .
rm -fr __MACOSX The\ Unarchiver
# recursively remove executable bit from every file, skipping directories
find . -type f -print0 | xargs -0 chmod -x

%build
export OBJCFLAGS="${RPM_OPT_FLAGS}"
make -C XADMaster -f Makefile.linux

%install
install -d %{buildroot}%{_bindir}
install -pm755 XADMaster/unar XADMaster/lsar %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -pm644 Extra/*.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 Extra/lsar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lsar
install -pm644 Extra/unar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/unar

%files
%license License.txt
%{_bindir}/lsar
%{_bindir}/unar
%{_mandir}/man1/*.1*
%{_datadir}/bash-completion/

%changelog
* Mon May 18 2020 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-17
- Rebuild for ICU 67

* Sat Apr 18 2020 Sérgio Basto <sergio@serjux.com> - 1.10.1-16
- Rebuild for gnustep 1.27.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-14
- Rebuild for ICU 65

* Fri Sep 06 2019 Sérgio Basto <sergio@serjux.com> - 1.10.1-13
- Rebuild for new gnustep 1.26.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-10
- Rebuild for ICU 63

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
- https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-8
- Rebuild for ICU 61.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-6
- Rebuild for ICU 60.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 16 2017 Sérgio Basto <sergio@serjux.com> - 1.10.1-3
- Rebuild (libgnustep-base)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 09 2016 Pete Walter <pwalter@fedoraproject.org> - 1.10.1-1
- Update to 1.10.1

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.8.1-12
- rebuild for ICU 57.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.8.1-10
- rebuild for ICU 56.1

* Tue Jul 14 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.1-9
- Remove LDFLAGS, pass RPM_OPT_FLAGS as OBJCFLAGS
  (Fix F23FTBFS, RHBZ#1240023).
- Add %%license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.8.1-7
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.8.1-6
- rebuild for ICU 53.1

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 20 2014 Christopher Meng <rpm@cicku.me> - 1.8.1-4
- Insert Fedora-specific LDFLAGS for linking

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Adam Williamson <awilliam@redhat.com> - 1.8.1-2
- rebuild for new icu

* Sat Jan 25 2014 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8.1-1
- upstream release 1.8.1 (rhbz#1047226)

* Sun Dec 29 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.8-1
- upstream release 1.8 (rhbz#1047226)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-4
- fix spurious executable permissions 

* Fri Apr 19 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-3
- revert dir ownership change and requires on bash-completion

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-2
- fix dir ownership and add requires on bash-completion. 
- fix a couple of typos

* Thu Apr 18 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 1.6-1
- initial spec file. based on spec from Huaren Zhong <huaren.zhong@gmail.com> 
