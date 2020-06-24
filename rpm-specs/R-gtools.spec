%global packname gtools
%global packver  3.8.2
%global rlibdir  %{_libdir}/R/library

# Some tests use the network.
%bcond_with network

Name:             R-%{packname}
Version:          3.8.2
Release:          2%{?dist}
Summary:          Various R Programming Tools

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods, R-stats, R-utils
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-utils

%description
Functions to assist in R programming, including:
    - assist in developing, updating, and maintaining R and R packages,
    - calculate the logit and inverse logit transformations,
    - test if a value is missing, empty or contains only NA and NULL values,
    - manipulate R's .Last function,
    - define macros,
    - detect odd and even integers,
    - convert strings containing non-ASCII characters (like single quotes) to
      plain ASCII,
    - perform a binary search,
    - sort strings containing both numeric and character components,
    - create a factor variable from the quantiles of a continuous variable,
    - enumerate permutations and combinations,
    - calculate and convert between fold-change and log-ratio,
    - calculate probabilities and generate random numbers from Dirichlet
      distributions,
    - apply a function over adjacent subsets of a vector,
    - modify the TCP_NODELAY flag for socket objects,
    - efficient 'rbind' of data frames, even if the column names don't match,
    - generate significance stars from p-values,
    - convert characters to/from ASCII codes,
    - convert character vector to ASCII representation.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
# No network for examples that check R version.
rm %{packname}/tests/test_setTCPNoDelay.R
%{_bindir}/R CMD check %{packname} --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 3.8.2-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.1-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.8.1-1
- Update to latest version

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.5.0-2
- rebuild for R 3.5.0

* Tue Mar 13 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.5.0-1
- initial package for Fedora
