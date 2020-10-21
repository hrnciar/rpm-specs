Name:           pmars
Version:        0.9.2
Release:        22%{?dist}
Summary:        Portable corewar system with ICWS'94 extensions

License:        GPLv2+
URL:            http://www.koth.org/pmars/
Source0:        http://downloads.sourceforge.net/corewar/%{name}-%{version}.tar.gz
# Patch to disable stripping of binary in spec file
Patch0:         pmars-0.9.2-nostrip.patch
#Show compiler commands
Patch1:         pmars-0.9.2-CCat.patch
Patch2:         pmars-sfprintf-format.patch
BuildRequires:  gcc
BuildRequires:  libX11-devel
Requires:       xorg-x11-fonts-75dpi

%description
pMARS is a Memory Array Redcode Simulator (MARS) for corewar.

    * portable, run it on your Mac at home or VAX at work
    * free and comes with source
    * core displays for DOS, Mac and UNIX
    * implements a new redcode dialect, ICWS'94, while remaining compatible
      with ICWS'88
    * powerful redcode extensions: multi-line EQUates, FOR/ROF text repetition
    * one of the fastest simulators written in a high level language
    * full-featured, programmable debugger
    * runs the automated tournament "KotH" at http://www.koth.org and
      http://www.ecst.csuchico.edu/~pizza/koth/ and the annual ICWS tournaments

%prep
%setup -q
%patch0 -p0 -b .nostrip
%patch1 -p0 -b .CCat
%patch2 -p0 -b .printf

# Make temporary doc dir
mkdir doc_install
cp -a doc doc_install
rm doc_install/doc/pmars.6


%build
make -C src CFLAGS="%{optflags} -DEXT94 -DXWINGRAPHX -DPERMUTATE"


%install
rm -rf %{buildroot}
install -D -p -m 755 src/pmars %{buildroot}%{_bindir}/pmars
install -D -p -m 644 doc/pmars.6 %{buildroot}%{_mandir}/man6/pmars.6



%files
%doc AUTHORS ChangeLog CONTRIB COPYING README config/ doc_install/doc/ warriors/
%{_bindir}/pmars
%{_mandir}/man6/pmars.6.*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 Jon Ciesla <limburgher@gmail.com> - 0.9.2-10
- Fix format-security FTBFS, BZ 1037252.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 0.9.2-3
- Moved doc manipulation to after patch application.

* Thu May 06 2010 Jon Ciesla <limb@jcomserv.net> - 0.9.2-3
- Fixed typos, macros, build and installation.

* Fri Apr 30 2010 Jon Ciesla <limb@jcomserv.net> - 0.9.2-2
- Added dep on xorg-x11-fonts-75dpi.
- Culled duplicate man page.

* Thu Apr 29 2010 Jon Ciesla <limb@jcomserv.net> - 0.9.2-1
- First build.
