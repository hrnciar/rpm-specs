%global packname remotes
%global packver  2.2.0
%global rlibdir  %{_datadir}/R/library

# Tests require the network.
%bcond_with network

Name:             R-%{packname}
Version:          2.2.0
Release:          2%{?dist}
Summary:          R Package Installation from Remote Repositories

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-stats, R-tools, R-utils
# Suggests:  R-brew, R-callr, R-codetools, R-curl, R-covr, R-git2r >= 0.23.0, R-knitr, R-mockery, R-pkgbuild >= 1.0.1, R-pingr, R-rmarkdown, R-rprojroot, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-brew
BuildRequires:    R-callr
BuildRequires:    R-codetools
BuildRequires:    R-curl
BuildRequires:    R-git2r >= 0.23.0
BuildRequires:    R-knitr
BuildRequires:    R-mockery
BuildRequires:    R-pkgbuild >= 1.0.1
BuildRequires:    R-pingr
BuildRequires:    R-rmarkdown
BuildRequires:    R-rprojroot
BuildRequires:    R-testthat
BuildRequires:    R-withr

%description
Download and install R packages stored in GitHub, GitLab, Bitbucket,
Bioconductor, or plain subversion or git repositories. This package provides
the 'install_*' functions in devtools. Indeed most of the code was copied over
from devtools.


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

# FIXME: Why does this not install?
install -p %{packname}/{README,NEWS}.md %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-tests --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/install-github.R
%{rlibdir}/%{packname}/install-github.Rin


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 2.1.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.4-1
- Update to latest version

* Tue Apr 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.3-1
- Update to latest version

* Fri Feb 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- initial package for Fedora
