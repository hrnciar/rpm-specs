%global packname  argon2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          9%{?dist}
Summary:          Secure Password Hashing

License:          BSD
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
Patch0001:        0001-Build-against-system-libraries.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel tex(latex)
BuildRequires:    libargon2-devel >= 20161029
BuildRequires:    libb2-devel

%description
Utilities for secure password hashing via the argon2 algorithm. It is a
relatively new hashing algorithm and is believed to be very secure. The
'argon2' implementation included in the package is the reference
implementation.  The package also includes some utilities that should be
useful for digest authentication, including a wrapper of 'blake2b'.  For
similar R packages, see sodium and 'bcrypt'.  See
<https://en.wikipedia.org/wiki/Argon2> or
<https://eprint.iacr.org/2015/430.pdf> for more information.


%prep
%setup -q -c -n %{packname}

# Delete bundled libraries.
pushd %{packname}
rm -r src/argon2
%patch0001 -p1
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
%doc %{rlibdir}/%{packname}/CITATION
%license %{rlibdir}/%{packname}/COPYRIGHTS
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.og> - 0.2.0-9
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-7
- rebuilt

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Remi Collet <remi@fedoraproject.org> - 0.2.0-5
- rebuild for libargon2 new soname

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.0-2
- rebuild for R 3.5.0

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.2.0-1
- initial package for Fedora
