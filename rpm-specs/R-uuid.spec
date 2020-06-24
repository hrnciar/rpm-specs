%global packname uuid
%global packver  0.1-4
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1.4
Release:          2%{?dist}
Summary:          Tools for generating and handling of UUIDs

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    libuuid-devel

%description
Tools for generating and handling of UUIDs (Universally Unique
Identifiers).


%prep
%setup -q -c -n %{packname}

# Use system libuuid.
pushd %{packname}
rm configure.ac configure src/Makevars.in src/[a-z]*.[ch]
sed -i -e '/configure/d' -e '/Makevars/d' -e '/src\/[a-z].*.[ch]/d' MD5
rm -r src/config.h.in src/win32
sed -i -e '/config.h/d' MD5
cat > src/Makevars << EOF
PKG_CFLAGS = \$(shell pkg-config --cflags uuid)
PKG_LIBS = \$(shell pkg-config --libs uuid)
EOF
popd


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
%doc %{rlibdir}/%{packname}/NEWS
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.1.4-2
- rebuild for R 4

* Wed Feb 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.1.2-5
- rebuild for R 3.5.0

* Wed May 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1.2-4
- Unbundle libuuid

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.1.2-2
- Add explicit directory listings.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.1.2-1
- initial package for Fedora
