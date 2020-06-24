%bcond_with check

%global packname processx
%global packver  3.4.2
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.4.2
Release:          2%{?dist}
Summary:          Execute and Control System Processes

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
# Fix curl test with no network.
Patch0001:        https://github.com/r-lib/processx/commit/4e3715af514b0187bd47d87e8fd99e17ad1d341c.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-ps >= 1.2.0, R-R6, R-utils
# Suggests:  R-callr >= 3.2.0, R-codetools, R-covr, R-crayon, R-curl, R-debugme, R-parallel, R-testthat, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-ps >= 1.2.0
BuildRequires:    R-R6
BuildRequires:    R-utils
%if %{with check}
BuildRequires:    R-callr >= 3.2.0
BuildRequires:    R-codetools
BuildRequires:    R-crayon
BuildRequires:    R-curl
BuildRequires:    R-debugme
BuildRequires:    R-parallel
BuildRequires:    R-testthat
BuildRequires:    R-withr
%endif

%description
Tools to run system processes in the background. It can check if a
background process is running; wait on a background process to finish; get
the exit status of finished processes; kill background processes. It can
read the standard output and error of the processes, using non-blocking
connections. 'processx' can poll a process for standard output or error,
with a timeout. It can also poll several processes at once.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME: Why does this not install?
install -pm 0644 %{packname}/README.md %{buildroot}%{rlibdir}/%{packname}/


%check
%if %{with check}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/README.md
%doc %{rlibdir}/%{packname}/CODE_OF_CONDUCT.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/bin
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/libs/client.so


%changelog
* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 3.4.2-2
- rebuild for R 4
- conditionalize check to break testthat loop

* Wed Feb 12 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.2-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.1-1
- Update to latest version

* Tue Jul 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.4.0-1
- Update to latest version

* Wed May 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.1-1
- Update to latest version

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3.0-1
- Update to latest version

* Wed Mar 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-2
- Enable more tests

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.1.0-1
- update to 3.1.0

* Mon May 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.0.3-1
- Update to latest version

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0.1-1
- initial package for Fedora
