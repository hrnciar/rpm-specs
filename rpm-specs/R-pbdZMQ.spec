%global packname  pbdZMQ
%global packvers  0.3-3
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.3
Release:          10%{?dist}
Summary:          Programming with Big Data -- Interface to ZeroMQ

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz
# https://github.com/snoweye/pbdZMQ/pull/38
Patch0001:        fix-configure.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-R6
# Suggests:  R-pbdRPC
# LinkingTo:
# Enhances:

BuildRequires:    R-devel tex(latex)
BuildRequires:    R-R6
BuildRequires:    R-pbdRPC
BuildRequires:    zeromq-devel >= 4.0.4

%description
'ZeroMQ' is a well-known library for high-performance asynchronous
messaging in scalable, distributed applications.  This package provides
high level R wrapper functions to easily utilize 'ZeroMQ'. We mainly focus
on interactive client/server programming frameworks.


%prep
%setup -q -c -n %{packname}
pushd %{packname}
%patch0001 -p1
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname} \
    --configure-args="--disable-internal-zmq"
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# ZeroMQ copyright is installed even though internal build is disabled.
rm -r %{buildroot}%{rlibdir}/%{packname}/zmq_copyright


%check
%{_bindir}/R CMD check %{packname}


%files
%license %{packname}/COPYING
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%dir %{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/etc/Makeconf
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/libs


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.3.3-8
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.3.3-2
- rebuild for R 3.5.0

* Sun May 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version.

* Wed Mar 07 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-4
- Move R-pbdRPC to Suggests.

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-3
- Fix path to license file.

* Tue Aug 29 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-2
- Add explicit directory listings.
- Add license file to rpm.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.6-1
- initial package for Fedora
