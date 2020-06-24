%global packname  geepack
%global packver   1.3
%global packrel   1
%global rlibdir   %{_libdir}/R/library

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          3%{?dist}
Summary:          Generalized Estimating Equation Package

License:          GPLv3+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-MASS, R-broom, R-magrittr
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(boxedminipage.sty)
BuildRequires:    R-methods
BuildRequires:    R-MASS
BuildRequires:    R-broom
BuildRequires:    R-magrittr

%description
Generalized estimating equations solver for parameters in mean, scale, and
correlation structures, through mean link, scale link, and correlation
link. Can also handle clustered categorical responses.

%package devel
Summary:          Development files for %{name}
Requires:         %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.


%prep
%setup -q -c -n %{packname}

for file in %{packname}/inst/doc/geepack-manual.Rnw; do
    iconv --from=latin1 --to=UTF-8 ${file} > ${file}.new
    touch -r ${file} ${file}.new
    sed "s|\r||g" ${file}.new > ${file}
    touch -r ${file}.new ${file}
    rm ${file}.new
done

# Fix permissions.
pushd %{packname}
chmod -x ChangeLog DESCRIPTION NAMESPACE inst/CITATION
chmod -x inst/CITATION inst/doc/* inst/include/*.h inst/include/tnt/*.h
chmod -x data/* man/* R/* src/* vignettes/*
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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so

%files devel
%{rlibdir}/%{packname}/include/


%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.1-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-4
- Fix some file permissions

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.2.1-3
- rebuild for R 3.5.0

* Thu Mar 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-2
- Fix some file line endings

* Tue Mar 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- initial package for Fedora
