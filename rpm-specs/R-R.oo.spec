%global packname  R.oo
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.23.0
Release:          3%{?dist}
Summary:          R Object-Oriented Programming with or without References

License:          LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-R.methodsS3 >= 1.7.1
# Imports:   R-methods, R-utils
# Suggests:  R-tools
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-R.methodsS3 >= 1.7.1
BuildRequires:    R-methods
BuildRequires:    R-utils
BuildRequires:    R-tools

%description
Methods and classes for object-oriented programming in R with or without
references.  Large effort has been made on making definition of methods as
simple as possible with a minimum of maintenance for package developers.
The package has been developed since 2001 and is now considered very
stable.  This is a cross-platform package implemented in pure R that
defines standard S3 classes without any tricks.


%prep
%setup -q -c -n %{packname}

# Fix line endings.
for file in %{packname}/inst/CITATION; do
    sed "s|\r||g" ${file} > ${file}.new
    touch -r ${file} ${file}.new
    mv ${file}.new ${file}
done
# Fix encoding.
file=%{packname}/NEWS
iconv -f latin1 -t UTF-8 ${file} > ${file}.new
touch -r ${file} ${file}.new
mv ${file}.new ${file}


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/misc


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.23.0-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.23.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-5
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.22.0-1
- Update to latest version

* Fri Mar 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21.0-3
- Fix some file permissions

* Thu Mar 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21.0-2
- Fix some file line endings and encodings

* Wed Mar 21 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.21.0-1
- initial package for Fedora
