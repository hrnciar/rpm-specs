%global packname bit
%global packver  1.1-15.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.15.2
Release:          2%{?dist}
Summary:          Class for vectors of 1-bit booleans

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)

%description
True boolean datatype (no NAs), coercion from and to logicals, integers and
integer subscripts; fast boolean operators and fast summary statistics. With
'bit' vectors you can store true binary booleans {FALSE,TRUE} at the expense of
1 bit only, on a 32 bit architecture this means factor 32 less RAM and ~ factor
32 more speed on boolean operations. Due to overhead of R calls, actual speed
gain depends on the size of the vector: expect gains for vectors of size >
10000 elements. Even for one-time boolean operations it can pay-off to convert
to bit, the pay-off is obvious, when such components are used more than once.
Reading from and writing to bit is approximately as fast as accessing standard
logicals - mostly due to R's time for memory allocation. The package allows to
work with pre-allocated memory for return values by calling .Call() directly:
when evaluating the speed of C-access with pre-allocated vector memory, coping
from bit to logical requires only 70% of the time for copying from logical to
logical; and copying from logical to bit comes at a performance penalty of
150%. the package now contains further classes for representing logical
selections: 'bitwhich' for very skewed selections and 'ri' for selecting ranges
of values for chunked processing. All three index classes can be used for
subsetting 'ff' objects (ff-2.1-0 and higher).


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# We don't care about these development files.
rm -r %{buildroot}%{rlibdir}/%{packname}/exec


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/ANNOUNCEMENT-1.0.txt
%doc %{rlibdir}/%{packname}/README_devel.txt
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.15.2-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.15.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.14-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.1.13-1
- update to 1.1-13, rebuild for R 3.5.0

* Thu Mar 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.12-2
- Fix file encodings and line endings.

* Thu Mar 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.12-1
- initial package for Fedora
