%global packname gplots
%global packver  3.1.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          3.1.0
Release:          1%{?dist}
Summary:          Various R Programming Tools for Plotting Data

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-gtools, R-stats, R-caTools, R-KernSmooth
# Suggests:  R-grid, R-MASS, R-knitr
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-gtools
BuildRequires:    R-stats
BuildRequires:    R-caTools
BuildRequires:    R-KernSmooth
BuildRequires:    R-grid
BuildRequires:    R-MASS
BuildRequires:    R-knitr

%description
Various R programming tools for plotting data, including:
- calculating and plotting locally smoothed summary function,
- enhanced versions of standard plots,
- manipulating colors,
- calculating and plotting two-dimensional data summaries,
- enhanced regression diagnostic plots,
- formula-enabled interface to 'stats::lowess' function,
- displaying textual data in plots,
- plotting a matrix where each cell contains a dot whose size reflects the
  relative magnitude of the elements,
- plotting "Venn" diagrams,
- displaying Open-Office style plots,
- plotting multiple data on same region, with separate axes,
- plotting means and confidence intervals,
- spacing points in an x-y plot so they don't overlap.


%prep
%setup -q -c -n %{packname}

# Fix line endings.
for file in %{packname}/inst/doc/venn.Rnw; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done


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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data


%changelog
* Fri Sep 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.0-1
- Update to latest version (#1880401)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.4-1
- Update to latest version

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 3.0.3-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1-1
- initial package for Fedora
