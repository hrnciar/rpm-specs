%global packname tidyr
%global packver  1.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          1%{?dist}
Summary:          Tidy Messy Data

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-dplyr >= 0.8.2, R-ellipsis >= 0.1.0, R-glue, R-magrittr, R-purrr, R-Rcpp, R-rlang, R-stringi, R-tibble >= 2.1.1, R-tidyselect >= 1.1.0, R-utils, R-vctrs >= 0.3.0, R-lifecycle
# Suggests:  R-covr, R-jsonlite, R-knitr, R-repurrrsive >= 1.0.0, R-rmarkdown, R-readr, R-testthat >= 2.1.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-dplyr >= 0.8.2
BuildRequires:    R-ellipsis >= 0.1.0
BuildRequires:    R-glue
BuildRequires:    R-magrittr
BuildRequires:    R-purrr
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-rlang
BuildRequires:    R-stringi
BuildRequires:    R-tibble >= 2.1.1
BuildRequires:    R-tidyselect >= 1.1.0
BuildRequires:    R-utils
BuildRequires:    R-vctrs >= 0.3.0
BuildRequires:    R-lifecycle
BuildRequires:    R-jsonlite
BuildRequires:    R-knitr
BuildRequires:    R-repurrrsive >= 1.0.0
BuildRequires:    R-rmarkdown
BuildRequires:    R-readr
BuildRequires:    R-testthat >= 2.1.0

%description
Tools to help to create tidy data, where each column is a variable, each row is
an observation, and each cell contains a single value. 'tidyr' contains tools
for changing the shape (pivoting) and hierarchy (nesting and 'unnesting') of a
dataset, turning deeply nested lists into rectangular data frames
('rectangling'), and extracting values out of string columns.  It also includes
tools for working with missing values (both implicit and explicit).


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data


%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.0.2-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.3-1
- initial package for Fedora
