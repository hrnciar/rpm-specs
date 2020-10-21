Name:           vinci
Version:        1.0.5
Release:        19%{?dist}
Summary:        Algorithms for volume computation

License:        GPL+
URL:            http://www.math.u-bordeaux1.fr/~aenge/index.php?category=software&page=vinci
Source0:        http://www.math.u-bordeaux1.fr/~aenge/software/%{name}/%{name}-%{version}.tar.gz
# Man page written by Jerry James using text found in the sources.  Therefore,
# the man page has the same copyright and license as the sources.
Source1:        %{name}.1

BuildRequires:  gcc
BuildRequires:  tex(latex)
Requires:       lrslib-utils

%description
The volume is one of the central properties of a convex body, and volume
computation is involved in many hard problems.  Applications range from
rather classical ones as in convex optimization to problems in remote
fields like algebraic geometry where the number of common roots of
polynomials can be related to a special polytope volume.

Part of the fascination of the subject stems from the discrepancy
between the intuitive notion of "volume" and the actual hardness of
computing it.  Despite this discouraging complexity - algorithms in
general need exponential time in the input dimension - steadily growing
computer power enables us to attack problems of practical interest.

Vinci is an easy to install C package that implements the state of the
art algorithms for volume computation.  It is the fruit of a research
project carried out at the IFOR (Institute for Operations Research) at
ETH Zürich, in collaboration with Benno Büeler and Komei Fukuda.

%prep
%setup -q

# Link with the right flags
sed -i "s|-o vinci|& $RPM_LD_FLAGS|" makefile

%build
make %{?_smp_mflags} OPT="$RPM_OPT_FLAGS"
pdflatex manual.tex
pdflatex manual.tex

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
sed -e "s/@VERSION@/%{version}/" %{SOURCE1} > \
  $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
touch -r %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog manual.pdf
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.0.5-9
- Use license macro
- Fix sed expression separator for new RPM_LD_FLAGS

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr  7 2014 Jerry James <loganjerry@gmail.com> - 1.0.5-6
- Update project and source URLs
- Link with RPM_LD_FLAGS

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Jerry James <loganjerry@gmail.com> - 1.0.5-2
- Fix permissions on the binary

* Tue Feb 14 2012 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Initial RPM
