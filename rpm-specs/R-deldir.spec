%global packname deldir
%global packver  0.1-25
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1.25
Release:          2%{?dist}
Summary:          Delaunay Triangulation and Dirichlet (Voronoi) Tessellation

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-grDevices
# Suggests:  R-polyclip
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-graphics
BuildRequires:    R-grDevices
BuildRequires:    R-polyclip

%description
Calculates the Delaunay triangulation and the Dirichlet or Voronoi
tessellation (with respect to the entire plane) of a planar point set.
Plots triangulations and tessellations in various ways.  Clips
tessellations to sub-windows. Calculates perimeters of tessellations.
Summarises information about the tiles of the tessellation.


%prep
%setup -q -c -n %{packname}

# Remove extraneous source code.
rm -r %{packname}/inst/code.discarded
rm %{packname}/inst/ex.out
rm -r %{packname}/inst/ratfor
rm -r %{packname}/inst/SavedRatfor


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
%doc %{rlibdir}/%{packname}/READ_ME
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/err.list


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.25-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.25-1
- Update to latest version

* Sun Feb 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.23-3
- Fix rank mismatch build errors

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.23-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.22-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.22-1
- Update to latest version

* Sat Jun 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.21-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.16-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.1.15-2
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.15-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.14-1
- initial package for Fedora
