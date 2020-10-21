%global packname waldo
%global packver  0.2.2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Find Differences Between R Objects

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-diffobj, R-fansi, R-glue, R-methods, R-rematch2, R-rlang, R-tibble
# Suggests:  R-testthat, R-covr, R-R6
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-diffobj
BuildRequires:    R-fansi
BuildRequires:    R-glue
BuildRequires:    R-methods
BuildRequires:    R-rematch2
BuildRequires:    R-rlang
BuildRequires:    R-tibble
BuildRequires:    R-testthat
BuildRequires:    R-R6

%description
Compare complex R objects and reveal the key differences.  Designed
particularly for use in testing packages where being able to quickly
isolate key differences makes understanding test failures much easier.


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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Oct 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version (#1888855)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version (#1886503)

* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- initial package for Fedora
