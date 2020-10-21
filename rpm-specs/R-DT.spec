%global packname DT
%global packver  0.16
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.16
Release:          1%{?dist}
Summary:          R Wrapper of the JavaScript Library 'DataTables'

# Main: GPLv3; JavaScript files: MIT or ASL 2.0, see below
License:          GPLv3 and MIT and ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-htmltools >= 0.3.6, R-htmlwidgets >= 1.3, R-jsonlite >= 0.9.16, R-magrittr, R-crosstalk, R-promises
# Suggests:  R-knitr >= 1.8, R-rmarkdown, R-shiny >= 1.2.0, R-testit
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-htmltools >= 0.3.6
BuildRequires:    R-htmlwidgets >= 1.3
BuildRequires:    R-jsonlite >= 0.9.16
BuildRequires:    R-magrittr
BuildRequires:    R-crosstalk
BuildRequires:    R-promises
BuildRequires:    R-knitr >= 1.8
BuildRequires:    R-rmarkdown
BuildRequires:    R-shiny >= 1.2.0
BuildRequires:    R-testit

# MIT; inst/htmlwidgets/lib/jquery
Provides:         bundled(js-jquery1) = 1.12.4
# MIT; inst/htmlwidgets/lib/datatables*, inst/htmlwidgets/css/datatables-crosstalk.css
Provides:         bundled(jquery.dataTables) = 1.10.20
# MIT; inst/htmlwidgets/lib/nouislider
Provides:         bundled(jquery.nouislider) = 7.0.10
# MIT; inst/htmlwidgets/lib/nouislider
Provides:         bundled(jquery.nouislider) = 7.0.10
# ASL 2.0; inst/lib/selectize
Provides:         bundled(js-brianreavis-selectize) = 0.12.1

%description
Data objects in R can be rendered as HTML tables using the JavaScript library
'DataTables' (typically via R Markdown or Shiny). The 'DataTables' library has
been included in this R package. The package name 'DT' is an abbreviation of
'DataTables'.


%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/NEWS.Rd
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/htmlwidgets


%changelog
* Wed Oct 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- Update to latest version (#1888077)

* Sat Aug 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.15-1
- Update to latest version

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.14-1
- initial package for Fedora
