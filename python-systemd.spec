# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

Summary:	Python interface to systemd
Name:		python-systemd
Version:	236
Release:	1
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/%{name}-%{version}.tar.gz
BuildSystem:	meson
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libsystemd)

%description
Provides Python scripting interface to systemd.

%install -a
# meson install does not write PEP 376 metadata; importlib.metadata needs it.
mkdir -p %{buildroot}%{py_platsitedir}/systemd_python-%{version}.dist-info
cat > %{buildroot}%{py_platsitedir}/systemd_python-%{version}.dist-info/METADATA << EOF
Metadata-Version: 2.1
Name: systemd-python
Version: %{version}
Summary: Python interface for libsystemd
License: LGPL-2.1-or-later
EOF
echo rpm > %{buildroot}%{py_platsitedir}/systemd_python-%{version}.dist-info/INSTALLER

%files
%doc README.md LICENSE.txt NEWS
%dir %{py_platsitedir}/systemd
%dir %{py_platsitedir}/systemd/test
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/systemd/__pycache__/*
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/test/__pycache__/*
%{py_platsitedir}/systemd_python-%{version}.dist-info/
