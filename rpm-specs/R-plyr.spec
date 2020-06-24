%global packname plyr
%global packver  1.8.6
%global rlibdir  %{_libdir}/R/library

# Prevent loops and heavy dependencies.
%global with_suggests 0

Name:             R-%{packname}
Version:          1.8.6
Release:          2%{?dist}
Summary:          Tools for Splitting, Applying and Combining Data

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.11.0
# Suggests:  R-abind, R-covr, R-doParallel, R-foreach, R-iterators, R-itertools, R-tcltk, R-testthat
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.11.0
BuildRequires:    R-abind
BuildRequires:    R-testthat
%if 0%{with_suggests}
BuildRequires:    R-doParallel
BuildRequires:    R-foreach
BuildRequires:    R-iterators
BuildRequires:    R-itertools
BuildRequires:    R-tcltk
%endif

%description
A set of tools that solves a common set of problems: you need to break a big
problem down into manageable pieces, operate on each piece and then put all the
pieces back together. For example, you might want to fit a model to each
spatial location or time point in your study, summarise data by panels or
collapse high-dimensional arrays to simpler summary statistics. The development
of plyr has been generously supported by Becton Dickinson.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.8.6-2
- rebuild for R 4

* Tue Mar 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.6-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.5-1
- Update to latest version

* Wed Nov 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-13
- Exclude Suggests for unavailable packages

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-12
- Disable longer test suite entirely; it's too flaky

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-11
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-9
- Enable larger test suite

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.4-9
- Rewrite using new template

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.8.4-6
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.8.4-4
- Remove extra rm from install step.

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.8.4-3
- Re-add Rcpp runtime dependency.

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.8.4-2
- new package built with tito

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.8.4-1
- initial package for Fedora
