%bcond_without check

%global packname vctrs
%global packver  0.3.4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Vector Helpers

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ellipsis >= 0.2.0, R-digest, R-glue, R-rlang >= 0.4.7
# Suggests:  R-bit64, R-covr, R-crayon, R-dplyr >= 0.8.5, R-generics, R-knitr, R-pillar >= 1.4.4, R-pkgdown, R-rmarkdown, R-testthat >= 2.3.0, R-tibble, R-withr, R-xml2, R-waldo >= 0.2.0, R-zeallot
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ellipsis >= 0.2.0
BuildRequires:    R-digest
BuildRequires:    R-glue
BuildRequires:    R-rlang >= 0.4.7
%if %{with check}
BuildRequires:    R-bit64
BuildRequires:    R-crayon
BuildRequires:    R-dplyr >= 0.8.5
BuildRequires:    R-generics
BuildRequires:    R-knitr
BuildRequires:    R-pillar >= 1.4.4
BuildRequires:    R-pkgdown
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.3.0
BuildRequires:    R-tibble
BuildRequires:    R-withr
BuildRequires:    R-xml2
BuildRequires:    R-waldo >= 0.2.0
BuildRequires:    R-zeallot
%endif

%description
Defines new notions of prototype and size that are used to provide tools for
consistent and well-founded type-coercion and size-recycling, and are in turn
connected to ideas of type- and size-stability useful for analysing function
interfaces.


%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
# pkgdown appears to only be a maintenance thing.
sed -i 's/pkgdown, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include


%changelog
* Thu Sep 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-1
- Update to latest version (#1873347)

* Thu Sep 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-2
- Re-enable checks

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.0-2
- conditionalize check to break loops
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.4-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- Update to latest version

* Thu May 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.0-1
- initial package for Fedora
