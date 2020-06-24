%global packname simmer
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((rticles|simmer\\.plot)\\)

Name:           R-%{packname}
Version:        4.4.2
Release:        2%{?dist}
Summary:        Discrete-Event Simulation for R

License:        GPLv2+
URL:            https://cran.r-project.org/package=%{packname}
Source0:        %{url}&version=%{version}#/%{packname}_%{version}.tar.gz

BuildRequires:  R-devel >= 3.1.2
BuildRequires:  R-Rcpp-devel >= 0.12.9, R-BH-devel >= 1.62.0.1
BuildRequires:  R-magrittr, R-testthat
# BuildRequires:  R-knitr, R-rmarkdown, R-rticles, R-simmer.plot

%description
A process-oriented and trajectory-based Discrete-Event Simulation (DES)
package for R. It is designed as a generic yet powerful framework. The
architecture encloses a robust and fast simulation core written in 'C++'
with automatic monitoring capabilities. It provides a rich and flexible R
API that revolves around the concept of trajectory, a common path in the
simulation model for entities of the same type.
Documentation about 'simmer' is provided by several vignettes included in
this package, via the paper by Ucar, Smeets & Azcorra (2019,
<doi:10.18637/jss.v090.i02>), and the paper by Ucar, Hernández, Serrano &
Azcorra (2018, <doi:10.1109/MCOM.2018.1700960>); see 'citation("simmer")'
for details.

%package devel
Summary:        Development Files for R-%{packname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       R-core-devel%{?_isa}

%description devel
Header files for %{packname}.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

%files devel
%{rlibdir}/%{packname}/include

%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 4.4.2-2
- rebuild for R 4

* Sat Jun 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.2-1
- Update to 4.4.2

* Sat Apr 11 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.1-1
- Update to 4.4.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 4.4.0-1
- Update to 4.4.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3.0-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.3.0-1
- Update to 4.3.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.2.2-1
- Update to 4.2.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 10 2019 Iñaki Úcar <iucar@fedoraproject.org> - 4.2.1-1
- Update to 4.2.1

* Fri Nov 09 2018 Iñaki Úcar <iucar@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Wed Sep 19 2018 Iñaki Úcar <iucar@fedoraproject.org> - 4.0.1-1
- Update to 4.0.1
- Reflow indentations

* Mon Jul 30 2018 Iñaki Úcar <i.ucar86@gmail.com> - 4.0.0-2
- Capitalize summary
- Remove 'Group', not used in Fedora
- Remove rm of buildroot, not needed

* Mon Jul 30 2018 Iñaki Úcar <i.ucar86@gmail.com> - 4.0.0-1
- Initial package creation
