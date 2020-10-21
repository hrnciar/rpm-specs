%global packname git2r
%global packver  0.27.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.27.1
Release:          3%{?dist}
Summary:          Provides Access to Git Repositories

License:          GPLv2
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-graphics, R-utils
# Suggests:  R-getPass
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(libgit2) >= 0.26.0
BuildRequires:    R-graphics
BuildRequires:    R-utils
BuildRequires:    R-getPass

%description
Interface to the 'libgit2' library, which is a pure C implementation of the
'Git' core methods. Provides access to 'Git' repositories to extract data and
running some basic 'Git' commands.


%prep
%setup -q -c -n %{packname}

# Remove bundled libgit2.
pushd %{packname}
rm -r src/libgit2
sed -i '/libgit2/d' MD5
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
%doc %{rlibdir}/%{packname}/AUTHORS
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/COPYING
%license %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.27.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.27.1-1
- Update to latest version

* Mon Apr 27 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.26.1-5
- Rebuild against libgit2 1.x

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26.1-1
- Update to latest version

* Mon Jun 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.2-2
- rebuilt for libgit2 0.28

* Wed Mar 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.2-1
- Update to latest version

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.25.1-1
- Update to latest version

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.23.0-2
- Rebuild for libgit2 0.27.x

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.23.0-1
- Update latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.21.0-2
- rebuild for R 3.5.0

* Mon Apr 23 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21.0-1
- initial package for Fedora
