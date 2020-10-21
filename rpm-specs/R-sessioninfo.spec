%global packname  sessioninfo
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1.1
Release:          6%{?dist}
Summary:          R Session Information

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
# https://github.com/r-lib/sessioninfo/issues/34
Patch0001:        0001-Handle-missing-timezones-in-tests.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-cli, R-tools, R-utils, R-withr
# Suggests:  R-callr, R-covr, R-mockery, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-tools
BuildRequires:    R-utils
BuildRequires:    R-withr
BuildRequires:    R-callr
BuildRequires:    R-mockery
BuildRequires:    R-testthat

%description
Query and print information about the current R session. It is similar to
'utils::sessionInfo()', but includes more information about packages, and where
they were installed from.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname} || ( cat %{packname}.Rcheck/tests/*.Rout* && exit 1 )


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/README.markdown
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
