%global packname  repurrrsive
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Examples of Recursive Lists and Nested or Split Data Frames

License:          CC0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-tibble, R-utils
# Suggests:  R-gapminder, R-jsonlite, R-purrr, R-rprojroot, R-testthat >= 2.1.0, R-wesanderson, R-xml2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-tibble
BuildRequires:    R-utils
BuildRequires:    R-gapminder
BuildRequires:    R-jsonlite
BuildRequires:    R-purrr
BuildRequires:    R-rprojroot
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-wesanderson
BuildRequires:    R-xml2

%description
Recursive lists in the form of R objects, JSON, and XML, for use in teaching
and examples. Examples include color palettes, Game of Thrones characters,
GitHub users and repositories, music collections, and entities from the Star
Wars universe. Data from the gapminder package is also included, as a simple
data frame and in nested and split forms.


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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.0.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- initial package for Fedora
