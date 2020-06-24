%global packname  fs
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Cross-Platform File System Operations Based on 'libuv'

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
# Fedora-specific.
Patch0001:        0001-Use-system-libuv.patch
# Workaround for https://github.com/libuv/libuv/issues/2262
Patch0002:        0002-Initialize-stat-buf-to-be-zero.patch
# Fix issue where file.cc needs cstring.h
Patch0003:        0003-fix-cstring.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-methods, R-Rcpp
# Suggests:  R-testthat, R-covr, R-pillar >= 1.0.0, R-tibble >= 1.1.0, R-crayon, R-rmarkdown, R-knitr, R-withr, R-spelling
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libuv) >= 1.18.0
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-Rcpp-devel
BuildRequires:    R-testthat
BuildRequires:    R-pillar >= 1.0.0
BuildRequires:    R-tibble >= 1.1.0
BuildRequires:    R-crayon
BuildRequires:    R-rmarkdown
BuildRequires:    R-knitr
BuildRequires:    R-withr
BuildRequires:    R-spelling

%description
A cross-platform interface to file system operations, built on top of the
'libuv' C library.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Remove bundled libuv.
%patch0001 -p1
rm -rf src/libuv
sed -i -e '/libuv/d' MD5

%patch0002 -p1

%patch0003 -p1

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
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-1
- update to 1.4.1
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Sun May 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- Update to latest version
- Add workaround for libuv stat bug (https://github.com/libuv/libuv/issues/2262)

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.7-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.6-1
- initial package for Fedora
