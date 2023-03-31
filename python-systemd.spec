# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

Summary:	Python interface to systemd
Name:		python-systemd
Version:	234
Release:	7
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/%{name}-%{version}.tar.gz
Patch0001:	0001-journal-avoid-warning-about-deprecated-constant.patch
Patch0002:	0002-reader-make-PY_SSIZE_T_CLEAN.patch
Patch0003:	0003-test-make-sure-NOTIFY_SOCKET-is-unset-in-test.patch
Patch0004:	0004-python-systemd-namespaces.patch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libsystemd)

%description
Provides Python scripting interface to systemd.

%prep
%autosetup -p1

%build
%make_build PYTHON=%{__python}

%install
%make_install PYTHON=%{__python}

%files
%doc README.md LICENSE.txt NEWS
%dir %{py_platsitedir}/systemd
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/*.egg-info
