%global packname pkgcache
%global packver  1.1.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Cache 'CRAN'-Like Metadata and R Packages

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat, R-callr >= 2.0.4.9000, R-cli >= 2.0.0, R-curl >= 3.2, R-digest, R-filelock, R-glue, R-prettyunits, R-R6, R-processx >= 3.3.0.9001, R-rappdirs, R-rlang, R-tibble, R-tools, R-utils, R-uuid
# Suggests:  R-covr, R-debugme, R-desc, R-fs, R-jsonlite, R-mockery, R-pingr, R-presser, R-rprojroot, R-sessioninfo, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat
BuildRequires:    R-callr >= 2.0.4.9000
BuildRequires:    R-cli >= 2.0.0
BuildRequires:    R-curl >= 3.2
BuildRequires:    R-digest
BuildRequires:    R-filelock
BuildRequires:    R-glue
BuildRequires:    R-prettyunits
BuildRequires:    R-R6
BuildRequires:    R-processx >= 3.3.0.9001
BuildRequires:    R-rappdirs
BuildRequires:    R-rlang
BuildRequires:    R-tibble
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-uuid
BuildRequires:    R-covr
BuildRequires:    R-debugme
BuildRequires:    R-desc
BuildRequires:    R-fs
BuildRequires:    R-jsonlite
BuildRequires:    R-mockery
BuildRequires:    R-pingr
BuildRequires:    R-presser
BuildRequires:    R-rprojroot
BuildRequires:    R-sessioninfo
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
Metadata and package cache for CRAN-like repositories. This is a utility
package to be used by package management tools that want to take advantage
of caching.


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
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Sun Oct 11 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- Update to latest version (#1887160)

* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-2
- Fix tests when offline

* Sat Sep 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
