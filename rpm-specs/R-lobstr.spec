%global packname lobstr
%global packver  1.1.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Visualize R Data Structures with Trees

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-crayon, R-Rcpp, R-rlang >= 0.3.0
# Suggests:  R-covr, R-pillar, R-pkgdown, R-testthat
# LinkingTo: R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-crayon
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-rlang >= 0.3.0
BuildRequires:    R-pillar
BuildRequires:    R-pkgdown
BuildRequires:    R-testthat

%description
A set of tools for inspecting and understanding R data structures inspired by
str(). Includes ast() for visualizing abstract syntax trees, ref() for showing
shared references, cst() for showing call stack trees, and obj_size() for
computing object sizes.


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sun Sep 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
