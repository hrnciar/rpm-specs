%global packname  stringdist
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.5.5
Release:          3%{?dist}
Summary:          Approximate String Matching and String Distance Functions

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-parallel
# Suggests:  R-tinytest
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-parallel
BuildRequires:    R-tinytest

%description
Implements an approximate string matching version of R's native 'match'
function. Can calculate various string distances based on edits
(Damerau-Levenshtein, Hamming, Levenshtein, optimal sting alignment), qgrams
(q-gram, cosine, jaccard distance) or heuristic metrics (Jaro, Jaro-Winkler).
An implementation of soundex is provided as well. Distances can be computed
between character vectors while taking proper care of encoding or between
integer vectors representing generic sequences. This package is built for speed
and runs in parallel by using 'openMP'. An API for C or C++ is exposed as well.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Seems useless.
rm %{buildroot}%{rlibdir}/%{packname}/include/Doxyfile


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/tinytest

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.9.5.5-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.5.5-1
- Update to latest version

* Tue Oct 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.5.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.5.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.5.2-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.5.1-1
- Update to latest version

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.9.4.7-2
- rebuild for R 3.5.0

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4.7-1
- initial package for Fedora
