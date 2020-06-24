%global packname V8
%global packver  3.1.0
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.1.0
Release:          2%{?dist}
Summary:          Embedded JavaScript and WebAssembly Engine for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# nodejs does not build on all arches
ExclusiveArch:    %{nodejs_arches}

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.12, R-jsonlite >= 1.0, R-curl >= 1.0, R-utils
# Suggests:  R-testthat, R-knitr, R-rmarkdown
# LinkingTo:
# Enhances:

Requires:         js-underscore
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    v8-devel
BuildRequires:    web-assets-devel
BuildRequires:    js-underscore
BuildRequires:    R-Rcpp-devel >= 0.12.12
BuildRequires:    R-jsonlite >= 1.0
BuildRequires:    R-curl >= 1.0
BuildRequires:    R-utils
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    glyphicons-halflings-fonts

# This is not packaged and it's only used to make sure example docs build when
# offline anyway.
Provides:         bundled(js-crossfilter) = 1.3.12

%description
An R interface to V8: Google's open source JavaScript and WebAssembly engine.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Replace bundled copy with symlink to packaged version (note that this cannot
# be done in prep because R CMD INSTALL copies symlink targets.)
ln -sf %{_jsdir}/underscore/underscore-min.js \
    %{buildroot}%{rlibdir}/%{packname}/js/underscore.js


%check
export LANG=C.UTF-8
# Vignettes use the network.
%{_bindir}/R CMD check %{packname} --ignore-vignettes


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/js
%{rlibdir}/%{packname}/wasm
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org> - 3.1.0-2
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.1.0-1
- Update to latest version

* Sat Mar 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.2-1
- Update to latest version

* Tue Feb 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1-2
- Fix test on big-endian systems

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2-1
- Update to latest version

* Tue Apr 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1-1
- Update to latest version
- Switch to v8 provided by nodejs

* Fri Feb 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-7
- Fix unbundling of JavaScript files

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.5-5
- rebuild for R 3.5.0

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-4
- Add missing Rcpp Requires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-2
- Use jsdir macro for JavaScript files

* Thu Nov 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5-1
- initial package for Fedora
