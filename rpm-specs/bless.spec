#debug info would be empty due to no binarys
%global debug_package %{nil}

Name: bless
Version: 0.6.2
Release: 4%{?dist}
Summary: High quality, full featured hex editor    

License: GPLv2+        
URL: http://home.gna.org/bless/           
Source0: https://github.com/afrantzis/bless/archive/v%{version}.tar.gz
Patch1: bless-0.6.0-fixblessutilrange.patch
Patch2: bless-0.6.2-default-editmode-overwrite.patch

BuildRequires:  gcc
BuildRequires: mono-devel
BuildRequires: gtk-sharp2-devel     
BuildRequires: desktop-file-utils
BuildRequires: rarian-compat
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel

Requires: mono-core
Requires: gtk-sharp2

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Bless is a binary (hex) editor, a program that 
enables you to edit files as sequences of bytes.

%package doc
Summary: Bless user manual

%description doc
This package contains the documentation for the 
bless hex editor.

%prep
%setup -q
%patch1 -p1 -b .buildfixrange
%patch2 -p1 -b .editmodeoverwrite

%build
./autogen.sh
%configure --without-scrollkeeper
make %{?_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT%{docdir}/%{name}/bless.spec
rm -f $RPM_BUILD_ROOT%{docdir}/%{name}/INSTALL
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/bless.desktop

%files
%{_bindir}/bless
%{_libdir}/bless/
%{_datadir}/bless/
%{_datadir}/pixmaps/bless*
%{_datadir}/applications/bless.desktop

%files doc
%{_docdir}/bless/
%exclude %{_docdir}/bless/INSTALL
%{_datadir}/omf/bless/

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 08 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.2-2
- default edit mode is now Overwrite instead of Insert

* Wed Apr 08 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.2-1
- Update to new upstream release 0.6.2

* Thu Feb 20 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.0-29
- Fix build with new mono 6, fixing confusion about System.Range and Bless.Util.Range

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-20
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 02 2016 Adel Gadllah <adel.gadllah@gmail.com> - 0.6.0-18
- Use %%global instead of %%define

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> 0.6.0-16
- another fix for mono4

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.0-15
- Rebuild (mono4)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Rahul Sundaram <sundaram@fedoraproject.org> - 0.6.0-11
- remove vendor tag from desktop file. https://fedorahosted.org/fpc/ticket/247
- clean up spec to follow current guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 21 2011 Dan Horák <dan[at]danny.cz> - 0.6.0-7
- updated the supported arch list

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.6.0-5
- ExckudeArch sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon May 25 2009 Xavier Lamien <laxathom@fedoraproject.org> - 0.6.0-3
- Build arch ppc64.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 22 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.6.0-1
- Update to 0.6.0

* Sat Apr 05 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-5
- Fix build with mono-1.9+ RH #440761

* Fri Jan 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-5
- Add post and postun requires

* Fri Jan 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-4
- Add ExclusiveArch

* Thu Jan 03 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-3
- Don't make it a noarch package

* Thu Jan 03 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-2
- Fix scrollkeeper scriptlet

* Wed Jan 02 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.5.2-1
- Initial build
