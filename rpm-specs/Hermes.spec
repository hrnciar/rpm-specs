Name:           Hermes
Version:        1.3.3
Release:        34%{?dist}
Summary:        Pixel format conversion library
License:        LGPLv2+
# upstream is no more
URL:            http://web.archive.org/web/20040202225109/http://www.clanlib.org/hermes/
Source:         %{name}-%{version}.tar.bz2
Patch0:         Hermes-1.3.3-debian.patch
Patch1:         Hermes-1.3.3-64bit.patch
BuildRequires:  gcc
BuildRequires:  automake

%description
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

On x86 and MMX architectures, handwritten assembler routines are taking over
the job and doing it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C compiler
as there is no platform specific code but those are supported: DOS, Win32
(Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment), some BeOS
support.


%package        devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.


%prep
%setup -q
%patch0 -p1 -z .deb
%patch1 -p1 -z .64bit
# sigh the tarbal contains bad timestamps or so? Which cause autoxxx to run,
# this stops this:
touch src/hrconfig.h.in
# mark asm files as NOT needing execstack
for i in src/*.S; do
  echo '.section .note.GNU-stack,"",@progbits' >> $i
done
# Needed for ppc64, automake can't be run here
cp -f %{_datadir}/automake-*/config.* .


%build
%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc AUTHORS COPYING ChangeLog FAQ NEWS README TODO*
%{_libdir}/libHermes.so.*

%files devel
%doc docs/api/*.htm docs/api/*.txt docs/api/api.ps
%{_includedir}/Hermes
%{_libdir}/libHermes.so


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 09 2009 Robert Scheck <robert@fedoraproject.org> 1.3.3-16
- Solve the ppc64-redhat-linux-gnu configure target error

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.3-14
- Autorebuild for GCC 4.3

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3-13
- Update License tag for new Licensing Guidelines compliance

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3-12
- FE6 Rebuild

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.3-11
- Taking over as new maintainer
- Add a patch from Debian fixing some 64 bit issues and more importantly
  fix building with a recent toolchain.
- Fix some further 64 bit issues
- Remove static lib
- Add --disable-dependency-tracking, touch config.h.in to fix the timestamp
  instead of BR: automake, autoconf
- Mark asm files as NOT needing execstack, making us OK with new default
  SELinux targeted policy settings.

* Sun Jul 02 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.3.3-10
- rebuilt for devel, for upgrade path

* Sun Mar 05 2006 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.3.3-9
- rebuilt for FE5

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3.3-8
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Dec 04 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:1.3.3-o.fdr.6: remove commented parts from scriplets

* Sun Sep 07 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:1.3.3-0.fdr.5: put back epochs, change download URL

* Fri Jul 18 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 1.3.3-0.fdr.4: remove epoch business

* Sat Jul 05 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0:1.3.3-0.fdr.3: merged spec files

* Sat May 10 2003 Dams <anvil[AT]livna.org> 0:1.3.3-0.fdr.2
- buildroot -> RPM_BUILD_ROOT
- use tar.bz2 instead of tar.gz