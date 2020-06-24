%global date 20130714
%global checkout %{date}svn

Name:		CutyCapt
Version:	0
Release:	0.17.%{checkout}%{?dist}
Summary:	A small command-line utility to capture WebKit's rendering of a web page

License:	GPLv2+ and LGPLv2+
URL:		http://cutycapt.sourceforge.net/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export -r 10 svn://svn.code.sf.net/p/cutycapt/code/ cutycapt
# tar -C cutycapt -cJv CutyCapt -f cutycapt-%%{date}.tar.xz
Source0:	cutycapt-%{date}.tar.xz
# Upstream have been asked via email to include a copy of the license text.
Source1:    COPYING
Source2:    COPYING.lesser

# Fix QPrinter FTBFS
Patch0:     %{name}-0.4.20130714svn-Fix-QPrinter-FTBFS.patch

BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	qt5-qtsvg-devel

%description
CutyCapt is a small cross-platform command-line utility to capture WebKit's
rendering of a web page into a variety of vector and bitmap formats,
including SVG, PDF, PS, PNG, JPEG, TIFF, GIF, and BMP.


%prep
%setup -q -n CutyCapt
%patch0 -p1
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%{qmake_qt5}
make  %{?_smp_mflags}


%install
mkdir -p %{buildroot}%{_bindir}
install -p -m0755 CutyCapt %{buildroot}%{_bindir}/CutyCapt


%files
%doc COPYING COPYING.lesser
%{_bindir}/CutyCapt


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 0-0.8.20130714svn
- use %%qmake_qt5 macro to ensure proper build flags

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-0.6.20130714svn
- Rebuilt for GCC 5 C++11 ABI change

* Wed Oct 22 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0-0.5.20130714svn
- fix QPrinter FBTFS

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20130714svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0-0.2.20130714svn
- rename to CutyCapt
- include copies of both GPLv2 and LGPLv2.1
- amend License tag

* Thu Mar 27 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0-0.1.20130714svn
- initial package

