%global real_name DICOMAnonymizer
%global commit ed06792ec29bbe128110ec4f8c7184b7d0efbc9a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snap 20191125git%{shortcommit}

Name:    dicomanonymizer
Version: 1
Release: 0.4.%{?snap}%{?dist}
Summary: A multi-threaded anonymizer for DICOM files

License: Unlicense and MIT
URL:     https://github.com/mmiv-center/%{real_name}
Source0: %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0: 0001-use-system-gdcm.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: make
BuildRequires: gdcm-devel
BuildRequires: zlib-devel
BuildRequires: libxml2-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libxslt-devel

%description
A multi-threaded anonymizer for DICOM files implementing most of DICOM PS 3.15
AnnexE. Entries such as uid entries are replaced with hash values. This ensures
that partial runs of a studies DICOM files can be merged afterwards. This
project is written in C++ using the gdcm library and multiple threads to
accelerate processing. Warning: The operation performed by this tool is a 'soft'
de-identification. Instead of a white list of allowed tags the tool keeps a list
of tags known to frequently contain personal identifying information (PII) and
replaces only those. On the command line you specify a patient identifier
(PatientID/PatientName). Only if you do not keep a mapping of the new and the
old identifier this is considered an anonymization. If such a list exists the
operation performed is a de-identification (permits a later re-identification).

%prep
%autosetup -n %{real_name}-%{commit}

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{_target_platform}/anonymize %{buildroot}%{_bindir}/dicomanonymize

%files
%license LICENSE
%doc README.md
%{_bindir}/dicomanonymize

%changelog
* Tue Aug 11 2020 Alessio <alciregi@fedoraproject.org> - 1-0.1.20191125gited06792
- Using %cmake_build macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20191125gited06792
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191125gited06792
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Alessio <alciregi@fedoraproject.org> - 0-0.1.20191125gited06792
Initial commit
