%global packname servr
%global packver  0.17
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.17
Release:          1%{?dist}
Summary:          Simple HTTP Server to Serve Static Files or Dynamic Documents

License:          GPL+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-mime >= 0.2, R-httpuv >= 1.4.0, R-xfun, R-jsonlite
# Suggests:  R-tools, R-later, R-rstudioapi, R-knitr >= 1.9, R-rmarkdown
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-mime >= 0.2
BuildRequires:    R-httpuv >= 1.4.0
BuildRequires:    R-xfun
BuildRequires:    R-jsonlite
BuildRequires:    R-tools
BuildRequires:    R-later
BuildRequires:    R-rstudioapi
BuildRequires:    R-knitr >= 1.9
BuildRequires:    R-rmarkdown

%description
Start an HTTP server in R to serve static files, or dynamic documents that
can be converted to HTML files (e.g., R Markdown) under a given directory.


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/resources


%changelog
* Thu Jun 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17-1
- Update to 0.17

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.16-1
- initial package for Fedora
