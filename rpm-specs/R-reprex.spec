%global packname  reprex
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((devtools)\\)

# Not all available yet.
%global with_suggests 0

Name:             R-%{packname}
Version:          0.3.0
Release:          6%{?dist}
Summary:          Prepare Reproducible Example Code via the Clipboard

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0001:        0001-Fix-test-results-with-pandoc-2.5.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-callr >= 2.0.0, R-clipr >= 0.4.0, R-fs, R-rlang, R-rmarkdown, R-utils, R-whisker, R-withr
# Suggests:  R-covr, R-devtools, R-fortunes, R-knitr, R-miniUI, R-rprojroot, R-rstudioapi, R-shiny, R-styler >= 1.0.2, R-testthat >= 2.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pandoc >= 1.12.3
BuildRequires:    R-callr >= 2.0.0
BuildRequires:    R-clipr >= 0.4.0
BuildRequires:    R-fs
BuildRequires:    R-rlang
BuildRequires:    R-rmarkdown
BuildRequires:    R-utils
BuildRequires:    R-whisker
BuildRequires:    R-withr
BuildRequires:    R-fortunes
BuildRequires:    R-knitr
BuildRequires:    R-rprojroot
BuildRequires:    R-rstudioapi
%if %{fedora} > 29
BuildRequires:    R-shiny
%endif
BuildRequires:    R-testthat >= 2.0.0
%if %{with_suggests}
BuildRequires:    R-devtools
BuildRequires:    R-miniUI
BuildRequires:    R-styler >= 1.0.2
%endif

%description
Convenience wrapper that uses the 'rmarkdown' package to render small snippets
of code to target formats that include both code and output. The goal is to
encourage the sharing of small, reproducible, and runnable examples on
code-oriented websites, such as <https://stackoverflow.com> and
<https://github.com>, or in email. The user's clipboard is the default source
of input code and the default target for rendered output. 'reprex' also
extracts clean, runnable R code from various common formats, such as copy/paste
from an R session.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export NOT_CRAN=true
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


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
%{rlibdir}/%{packname}/addins
%{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/templates


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-3
- Remove explicit dependencies provided by automatic dependency generator
- Fix tests with pandoc 2.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Update to latest version
- Enable more tests

* Tue Apr 24 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-1
- initial package for Fedora
