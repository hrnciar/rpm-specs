Name:		gappa
Version:	1.3.5
Release:	7%{?dist}
Summary:	Prove programs with floating-point or fixed-point arithmetic

License:	GPLv2 or CeCILL
URL:		http://gappa.gforge.inria.fr/
Source0:	https://gforge.inria.fr/frs/download.php/file/38044/%{name}-%{version}.tar.gz
Patch0:         gappa-gcc11.patch

BuildRequires:	bison
BuildRequires:	boost-devel
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel
BuildRequires:	remake

# For documentation
BuildRequires:	dblatex
BuildRequires:	tex-courier
BuildRequires:	tex-ec
BuildRequires:	tex-helvetic
BuildRequires:	tex-rsfs
BuildRequires:	tex-symbol
BuildRequires:	tex-times
BuildRequires:	tex-zapfding
BuildRequires:	tex(mathrsfs.sty)
BuildRequires:	tex(multirow.sty)
BuildRequires:	tex(pdfpages.sty)

%description
Gappa is a tool intended to help verifying and formally prove
properties on numerical programs and circuits handling floating-point
or fixed-point arithmetic.  This tool manipulates logical formulas
stating the enclosures of expressions in some intervals.  Through the
use of rounding operators as part of the expressions, Gappa is specially
designed to deal with formulas that could appear when certifying numerical
codes. In particular, Gappa makes it simple to bound computational errors
due to floating-point arithmetic.  The tool and its documentation were
written by Guillaume Melquiond.

%prep
%autosetup -p0

# Fix encoding
iconv -f latin1 -t utf8 COPYING > COPYING.UTF8 && \
touch -r COPYING COPYING.UTF8 && \
mv COPYING.UTF8 COPYING

# Increase the test timeout for ARM
sed -i 's/timeout 5/&0/' Remakefile.in

%build
%configure
# Use the system remake
rm -f remake
ln -s %{_bindir}/remake remake
remake -d %{?_smp_mflags}
remake -d doc/gappa.pdf

%check
remake check

%install
sed -i 's|\(cp src/gappa \).*|\1%{buildroot}%{_bindir}|' Remakefile
mkdir -p %{buildroot}%{_bindir}
remake install


%files
%{_bindir}/gappa
%doc AUTHORS README.md NEWS.md doc/gappa.pdf
%license COPYING COPYING.GPL


%changelog
* Wed Jul 29 2020 Jeff Law <law@redhat.com> - 1.3.5-7
- Make comparison object invocable as const

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Petr Viktorin <pviktori@redhat.com> - 1.3.5-5
- Remove BuildRequires on python2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-3
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Jerry James <loganjerry@gmail.com> - 1.3.5-1
- New upstream version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 1.3.3-1
- New upstream version
- Drop upstreamed -vec patch

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul  6 2018 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Fix out of bounds vector accesses

* Mon Feb 12 2018 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- New upstream version

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.3.1-3
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Jerry James <loganjerry@gmail.com> - 1.3.1-1
- New upstream version

* Fri Jul 22 2016 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- New upstream version

* Fri Jun 24 2016 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- New upstream version

* Fri Feb 12 2016 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-6
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.2.0-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.2.0-3
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream version

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.2-2
- Rebuild for boost 1.57.0

* Tue Oct 21 2014 Jerry James <loganjerry@gmail.com> - 1.1.2-1
- New upstream version
- Fix license handling

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1.1.1-2
- Rebuild for boost 1.55.0

* Mon Mar 31 2014 Jerry James <loganjerry@gmail.com> - 1.1.1-1
- New upstream version

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream version
- Drop upstreamed patch and NEWS typo workaround

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.0.0-2
- Rebuild for boost 1.54.0

* Mon Jul 29 2013 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- New upstream version
- Drop version-specific short test; we rely on the upstream test suite

* Wed Jul  3 2013 Jerry James <loganjerry@gmail.com> - 0.18.0-1
- New upstream version

* Tue May 14 2013 Jerry James <loganjerry@gmail.com> - 0.17.1-1
- New upstream version

* Mon Feb 25 2013 Jerry James <loganjerry@gmail.com> - 0.16.6-1
- New upstream version

* Tue Feb 19 2013 Jerry James <loganjerry@gmail.com> - 0.16.5-1
- New upstream version
- Trim BRs now that tex(latex) Requires more packages

* Thu Feb 14 2013 Jerry James <loganjerry@gmail.com> - 0.16.3-2
- Add -dblatex patch to fix FTBFS

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan  7 2013 Jerry James <loganjerry@gmail.com> - 0.16.3-1
- New upstream version

* Wed Dec 26 2012 Jerry James <loganjerry@gmail.com> - 0.16.2-1
- New upstream version
- New BRs due to TeXLive 2012

* Mon Aug  6 2012 Jerry James <loganjerry@gmail.com> - 0.16.1-2
- Rebuild for boost 1.50

* Sat Jul 28 2012 Jerry James <loganjerry@gmail.com> - 0.16.1-1
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Jerry James <loganjerry@gmail.com> - 0.16.0-1
- New upstream version

* Sat Jan  7 2012 Jerry James <loganjerry@gmail.com> - 0.15.1-2
- Rebuild for GCC 4.7

* Thu Oct 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.15.1-1.2
- rebuild with new gmp without compat lib

* Mon Oct 10 2011 Peter Schiffer <pschiffe@redhat.com> - 0.15.1-1.1
- rebuild with new gmp

* Mon Sep 19 2011 Jerry James <loganjerry@gmail.com> - 0.15.1-1
- New upstream version

* Mon Jun  6 2011 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- New upstream version
- Drop defattr

* Tue Apr 19 2011 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- New upstream version
- Drop %%clean section
- Drop upstreamed patches
- Build the PDF file instead of downloading it

* Tue Mar 15 2011 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- New upstream version
- Remove BuildRoot tag
- Use flex and bison to regenerate the lexer and parser

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.13.0-5
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-4
- Removed now-incorrect comment.

* Sat Sep 11 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-3
- Removed documentation source code from package
- Greatly simplified spec file.

* Fri Sep 10 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-2
- Respond to comments 1-2 in https://bugzilla.redhat.com/show_bug.cgi?id=622173
- Simplify (drop variable definitions in configure, drop INSTALL file)
- Preserve the timestamp of file COPYING
- More macro use
- Modified to use bundled testsuite as well
- PDF manual added

* Sat Aug  7 2010 David A. Wheeler <dwheeler@dwheeler.com> - 0.13.0-1
- Initial packaging
