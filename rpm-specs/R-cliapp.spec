%global packname  cliapp
%global rlibdir  %{_datadir}/R/library

# Depends on callr, which depends on this.
%global with_loop 1

Name:             R-%{packname}
Version:          0.1.0
Release:          5%{?dist}
Summary:          Create Rich Command Line Applications

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-crayon, R-fansi, R-glue >= 1.3.0, R-prettycode, R-progress >= 1.2.0, R-R6, R-selectr, R-utils, R-withr, R-xml2
# Suggests:  R-callr, R-covr, R-rstudioapi, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-fansi
BuildRequires:    R-glue >= 1.3.0
BuildRequires:    R-prettycode
BuildRequires:    R-progress >= 1.2.0
BuildRequires:    R-R6
BuildRequires:    R-selectr
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-xml2
BuildRequires:    R-rstudioapi
BuildRequires:    R-testthat
%if %{with_loop}
BuildRequires:    R-callr
%endif

%description
Create rich command line applications, with colors, headings, lists, alerts,
progress bars, etc. It uses CSS for custom themes.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Fixup shebang.
for script in $(ls %{packname}/scripts/*.R); do
    sed -e '1d;2i#!%{_bindir}/Rscript' $script > ${script}.new && \
    touch -r $script ${script}.new && \
    mv ${script}.new $script
done


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_loop}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


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
%{rlibdir}/%{packname}/scripts


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora
