%global packname modelr
%global packver  0.1.8
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.1.8
Release:          2%{?dist}
Summary:          Modelling Functions that Work with the Pipe

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-broom, R-magrittr, R-purrr >= 0.2.2, R-rlang >= 0.2.0, R-tibble, R-tidyr >= 0.8.0, R-tidyselect, R-vctrs
# Suggests:  R-compiler, R-covr, R-ggplot2, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-broom
BuildRequires:    R-magrittr
BuildRequires:    R-purrr >= 0.2.2
BuildRequires:    R-rlang >= 0.2.0
BuildRequires:    R-tibble
BuildRequires:    R-tidyr >= 0.8.0
BuildRequires:    R-tidyselect
BuildRequires:    R-vctrs
BuildRequires:    R-compiler
BuildRequires:    R-ggplot2
BuildRequires:    R-testthat

%description
Functions for modelling that help you seamlessly integrate modelling into a
pipeline of data manipulation and visualisation.


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.8-2
- rebuild for R 4

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.8-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.6-1
- Update to latest version

* Thu Jan 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.5-1
- initial package for Fedora
